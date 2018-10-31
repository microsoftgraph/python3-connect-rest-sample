# [ARCHIVED] Microsoft Graph API Connect Sample for Python

## IMPORTANT

**This project is being archived and replaced with the [Build Python Django apps with Microsoft Graph](https://github.com/microsoftgraph/msgraph-training-pythondjangoapp). As part of the archival process, we're closing all open issues and pull requests.**

**You can continue to use this sample "as-is", but it won't be maintained moving forward. We apologize for any inconvenience.**

Connecting to Office 365 is the first step every app must take to start working
with Office 365 services and data. This sample shows how to connect and then
call one API through the Microsoft Graph API (previously called Office 365
unified API), and uses the Office Fabric UI to create an Office 365 experience.

<img src="./README assets/screenshot.PNG" alt="Python Connect sample screenshot" />

## Prerequisites

To use the Microsoft Graph API Connect sample for Python, you need the following:
* [Python 3.5.2](https://www.python.org/downloads/)
* [Flask-OAuthlib](https://github.com/lepture/flask-oauthlib)
* [Flask-Script 0.4](http://flask-script.readthedocs.io/en/latest/)
* [Requests module](http://docs.python-requests.org/en/latest/)
* A [Microsoft account](https://www.outlook.com/) or an [Office 365 for business account](https://msdn.microsoft.com/en-us/office/office365/howto/setup-development-environment#bk_Office365Account)

> Note: Microsoft has tested the [Flask-OAuthlib](https://github.com/lepture/flask-oauthlib) library in basic scenarios and confirmed that it works with the v2.0 endpoint. Microsoft does not provide fixes for this library and has not done a review of it. Issues and feature requests should be directed to the library’s open-source project.

## Register the application

Register an app on the Microsoft App Registration Portal. This generates the app ID and password that you'll use to configure the app for authentication.

1. Sign into the [Microsoft App Registration Portal](https://apps.dev.microsoft.com/) using either your personal or work or school account.

2. Choose **Add an app**.

3. Enter a name for the app, and choose **Create application**.

	The registration page displays, listing the properties of your app.

4. Copy the application ID. This is the unique identifier for your app.

5. Under **Application Secrets**, choose **Generate New Password**. Copy the app secret from the **New password generated** dialog.

	You'll use the application ID and app secret to configure the app.

6. Under **Platforms**, choose **Add platform** > **Web**.

7. Make sure the **Allow Implicit Flow** check box is selected, and enter *http://localhost:5000/login/authorized* as the Redirect URI.

	The **Allow Implicit Flow** option enables the OpenID Connect hybrid flow. During authentication, this enables the app to receive both sign-in info (the **id_token**) and artifacts (in this case, an authorization code) that the app uses to obtain an access token.

	The redirect URI *http://localhost:5000/login/authorized* is the value that the OmniAuth middleware is configured to use once it has processed the authentication request.

8. Choose **Save**.

## Configure and run the app

1. Using your favorite text editor, open the **_PRIVATE.txt** file.
2. Replace *ENTER_YOUR_CLIENT_ID* with the client ID of your registered application.
3. Replace *ENTER_YOUR_SECRET* with the key you generated for your app.
4. Start the development server by running ```python manage.py runserver```.
5. Navigate to ```http://localhost:5000/``` in your web browser.

To learn more about this sample, see [walkthrough.md](walkthrough.md).

<a name="contributing"></a>
## Contributing ##

If you'd like to contribute to this sample, see [CONTRIBUTING.MD](/CONTRIBUTING.md).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.  

## Questions and comments

We'd love to get your feedback about the Office 365 Python Connect sample. You can send your questions and suggestions to us in the [Issues](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues) section of this repository.

Your feedback is important to us. Connect with us on [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph). Tag your questions with [MicrosoftGraph] and [office365].
  
## Additional resources

* [Office Dev Center](http://dev.office.com/)
* [Microsoft Graph API](http://graph.microsoft.io)
* [Office UI Fabric](http://dev.office.com/fabric)

## Copyright
Copyright (c) 2016 Microsoft. All rights reserved.
