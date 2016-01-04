# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license. See full license at the bottom of this file.

import requests
import uuid
import json
from connect.data import get_email_text

# The base URL for the Microsoft Graph API.
graph_api_endpoint = 'https://graph.microsoft.com/v1.0{0}'
		
def call_sendMail_endpoint(access_token, alias, emailAddress):
	# The resource URL for the sendMail action.
  send_mail_url = graph_api_endpoint.format('/me/microsoft.graph.sendMail')
	
	# Set request headers.
  headers = { 
		'User-Agent' : 'python_tutorial/1.0',
		'Authorization' : 'Bearer {0}'.format(access_token),
		'Accept' : 'application/json',
		'Content-Type' : 'application/json'
	}
						
	# Use these headers to instrument calls. Makes it easier
	# to correlate requests and responses in case of problems
	# and is a recommended best practice.
  request_id = str(uuid.uuid4())
  instrumentation = { 
		'client-request-id' : request_id,
		'return-client-request-id' : 'true' 
	}
  headers.update(instrumentation)

	# Create the email that is to be sent with API.
  email = {
		'Message': {
			'Subject': 'Welcome to Office 365 development with Python and the Office 365 Connect sample',
			'Body': {
				'ContentType': 'HTML',
				'Content': get_email_text(alias)
			},
			'ToRecipients': [
				{
					'EmailAddress': {
						'Address': emailAddress
					}
				}
			]
		},
		'SaveToSentItems': 'true'
	}   

  response = requests.post(url = send_mail_url, headers = headers, data = json.dumps(email), params = None)

	# Check if the response is 202 (success) or not (failure).
  if (response.status_code == requests.codes.accepted):
    return response.status_code
  else:
    jsonResponse = json.loads(response.text)
    return jsonResponse['error']['code']

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