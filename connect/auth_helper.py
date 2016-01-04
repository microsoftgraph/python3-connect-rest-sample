# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license. See full license at the bottom of this file.

from urllib.parse import quote, urlencode
import base64
import json
import requests
from connect.config import client_id, client_secret

# The URL of the home page of the app. Leave as default if running on localhost:8000.
home_page_url = 'http://127.0.0.1:8000/'

# The OAuth authority.
authority = 'https://login.microsoftonline.com'

# The authorize URL that initiates the OAuth2 client credential flow for admin consent.
authorize_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/authorize?{0}')

# The token issuing endpoint.
token_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/token')

# The scopes required by the app.
scopes = [ 'openid', 'https://graph.microsoft.com/Mail.Send' ]

# This function creates the signin URL that the app will
# direct the user to in order to sign in to Office 365 and
# give the app consent.
def get_signin_url(redirect_uri):
  # Build the query parameters for the signin URL.
  params = { 'client_id': client_id,
             'redirect_uri': redirect_uri,
             'response_type': 'code',
             'scope': ' '.join(str(i) for i in scopes)
           }

  signin_url = authorize_url.format(urlencode(params))
  return signin_url
  
def get_signout_url(redirect_uri):
  params = { 'post_logout_redirect_uri': home_page_url
           }
           
  signout_url = (authority + '/common/oauth2/v2.0/logout?{0}').format(urlencode(params))
  return signout_url
  
# This function passes the authorization code to the token
# issuing endpoint, gets the token, and then returns it.
def get_token_from_code(auth_code, redirect_uri):
  # Build the post form for the token request
  post_data = { 'grant_type': 'authorization_code',
                'code': auth_code,
                'redirect_uri': redirect_uri,
                'client_id': client_id,
                'scope': ' '.join(str(i) for i in scopes),
                'client_secret': client_secret
              }
              
  r = requests.post(token_url, data = post_data)
  
  try:
    return r.json()
  except:
    return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)

# This function takes the access token and breaks it
# apart to get information about the user.
def get_user_info_from_token(id_token):
  # JWT is in three parts, header, token, and signature
  # separated by '.'.
  token_parts = id_token.split('.')
  encoded_token = token_parts[1]
  
  # Base64 strings should have a length divisible by 4.
  # If this one doesn't, add the '=' padding to fix it.
  leftovers = len(encoded_token) % 4
  if leftovers == 2:
      encoded_token += '=='
  elif leftovers == 3:
      encoded_token += '='
  
  # URL-safe base64 decode the token parts.
  decoded = base64.urlsafe_b64decode(encoded_token.encode('utf-8')).decode('utf-8')
  
  # Load decoded token into a JSON object.
  jwt = json.loads(decoded)
  
  return jwt
  
#######################################################################
#  
# O365-Python-Microsoft-Graph-Connect, https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect
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
