# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license. See full license at the bottom of this file.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from connect.auth_helper import get_signin_url, get_token_from_code, get_user_info_from_token
from connect.graph_service import call_sendMail_endpoint

# This is the home route. It renders a page with a button
# to connect to Office 365.
def home(request):
  redirect_uri = request.build_absolute_uri(reverse('connect:get_token'))
  sign_in_url = get_signin_url(redirect_uri)
  context = { 
    'sign_in_url': sign_in_url 
  }
  return render(request, 'connect/connect.html', context)

# This is the route that is the redirect URI of your registered
# Azuzre application. An authorization code is returned here that
# is swapped for an access token in auth_helper.
def get_token(request):
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('connect:get_token'))
  token = get_token_from_code(auth_code, redirect_uri)
  access_token = token['access_token']
  user_info = get_user_info_from_token(token['id_token'])

  # Save the token and other information for the view in the session.
  request.session['access_token'] = access_token
  request.session['name'] = user_info['given_name']
  request.session['emailAddress'] = user_info['upn']  
  request.session['showSuccess'] = 'false'
  request.session['showError'] = 'false'
  request.session['pageRefresh'] = 'true'
  return HttpResponseRedirect(reverse('connect:main'))
  
# This is the main view that is displayed after a user connects
# to Office 365. It shows a textbox that the user can enter an 
# email address to send an email to and a button to send the email.
def main(request):
  if request.session['pageRefresh'] == 'false':
    request.session['pageRefresh'] = 'true'
  else :
    request.session['showSuccess'] = 'false'  
    request.session['showError'] = 'false' 
  
  context = {
    'name': request.session['name'],
    'emailAddress': request.session['emailAddress'],
    'showSuccess': request.session['showSuccess'],
    'showError': request.session['showError']
  }
  return render(request, 'connect/main.html', context)
  
# This is the route that is called from the main.html template
# to send an email with the unified API.
def send_mail(request):
  # Change the stored email address to whatever the user put in the form.
  request.session['emailAddress'] = request.GET.get('emailAddress')
  
  response = call_sendMail_endpoint(request.session['access_token'], request.session['name'], request.session['emailAddress'])
  
  # The success code for /me/sendMail is 202. Check to make sure
  # that the operation completed successfully. 
  if response == 202:
    request.session['showSuccess'] = 'true'  
    request.session['showError'] = 'false'  
  else:
    print(response)
    request.session['showSuccess'] = 'false' 
    request.session['showError'] = 'true' 
  
  request.session['pageRefresh'] = 'false'
  return HttpResponseRedirect(reverse('connect:main'))
  
# This is the route that is called when the user clicks the disconnect
# button in the navigation bar. Clear user identifying information from
# the session and redirect to the home page. 
def disconnect(request):
  request.session['access_token'] = None
  request.session['name'] = None
  request.session['emailAddress'] = None
  return HttpResponseRedirect(reverse('connect:home'))
  
#######################################################################
#  
# O365-Python-Unified-API-Connect, https://github.com/OfficeDev/O365-Python-Unified-API-Connect
#
# Copyright (c) Microsoft Corporation
# All rights reserved.
#
# MIT License:
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#######################################################################