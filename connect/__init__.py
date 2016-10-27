# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.

from connect.config import client_id, client_secret
from connect.graph_service import call_sendMail_endpoint
from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from flask_oauthlib.client import OAuth, OAuthException
import json
from logging import Logger
import uuid

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

# Put your consumer key and consumer secret into a config file
# and don't check it into github!!
microsoft = oauth.remote_app(
	'microsoft',
	consumer_key=client_id,
	consumer_secret=client_secret,
	request_token_params={'scope': 'User.Read Mail.Send'},
	base_url='https://graph.microsoft.com/v1.0/',
	request_token_url=None,
	access_token_method='POST',
	access_token_url='https://login.microsoftonline.com/common/oauth2/v2.0/token',
	authorize_url='https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
)


@app.route('/')
def index():
	 return render_template('connect.html')


@app.route('/login')
def login():

	# Generate the guid to only accept initiated logins
	guid = uuid.uuid4()
	session['state'] = guid

	return microsoft.authorize(callback=url_for('authorized', _external=True), state=guid)

@app.route('/logout')
def logout():
	session.pop('microsoft_token', None)
	session.pop('state', None)
	return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
	response = microsoft.authorized_response()

	if response is None:
		return "Access Denied: Reason=%s\nError=%s" % (
			request.args['error'], 
			request.args['error_description']
		)

	# Check response for state
	if str(session['state']) != str(request.args['state']):
		raise Exception('State has been messed with, end authentication')
		
	# Okay to store this in a local variable, encrypt if it's going to client
	# machine or database. Treat as a password. 
	session['microsoft_token'] = (response['access_token'], '')
	# Store the token in another session variable for easy access
	session['access_token'] = response['access_token']
	meResponse = microsoft.get('me')
	meData = json.dumps(meResponse.data)
	me = json.loads(meData)
	userName = me['displayName']
	userEmailAddress = me['userPrincipalName']
	session['alias'] = userName
	return render_template('main.html', alias = userName, emailAddress=userEmailAddress)

@app.route('/main')
def main():
	return render_template('main.html')

# This is the route that is called from the main.html template
# to send an email with the Microsoft Graph API.
@app.route('/send_mail')
def send_mail():
  # Change the stored email address to whatever the user put in the form.
  emailAddress = request.args.get('emailAddress')
  response = call_sendMail_endpoint(session['access_token'], session['alias'], emailAddress)
  
  # The success code for /me/sendMail is 202. Check to make sure
  # that the operation completed successfully. 
  if response == 202:
    showSuccess = 'true'  
    showError = 'false'  
  else:
    print(response)
    showSuccess = 'false' 
    showError = 'true' 
  
  session['pageRefresh'] = 'false'
  return render_template('main.html', alias=session['alias'], emailAddress=emailAddress, showSuccess=showSuccess, showError=showError)


# If library is having trouble with refresh, uncomment below and implement refresh handler
# see https://github.com/lepture/flask-oauthlib/issues/160 for instructions on how to do this

# Implements refresh token logic
# @app.route('/refresh', methods=['POST'])
# def refresh():

@microsoft.tokengetter
def get_microsoft_oauth_token():
	return session.get('microsoft_token')

if __name__ == '__main__':
	app.run()
