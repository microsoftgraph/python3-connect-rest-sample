# Microsoft Graph を使った Office 365 Python Connect サンプル

各アプリで Office 365 のサービスとデータの操作を開始するため、最初に Office 365 に接続する必要があります。このサンプルでは、Microsoft Graph API (以前は Office 365 統合 API と呼ばれていた) を介して 1 つの API に接続して呼び出す方法を示し、Office Fabric UI を使って Office 365 エクスペリエンスを作成します。

> メモ: このサンプルをより迅速に実行するため、「[Office 365 API を使う](http://dev.office.com/getting-started/office365apis?platform=option-python#setup)」ページに記載された登録の簡略化をお試しください。

![Office 365 Python Connect サンプルのスクリーン ショット](./README assets/screenshot.PNG)

## 前提条件

Office 365 Python Connect サンプルを使うには、次が必要です。
* [Python 3.4.3](https://www.python.org/downloads/) 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* Office 365 アカウント。Office 365 アプリのビルドを開始するために必要なリソースを含む [Office 365 Developer サブスクリプション](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0)にサインアップできます。

         > メモ: サブスクリプションをすでにお持ちの場合、上記のリンクをクリックすると、「*申し訳ございません。現在のアカウントに追加できません*」というメッセージが表示されるページに移動します。その場合は、現在使っている Office 365 サブスクリプションのアカウントをご利用いただけます。
* アプリケーションを登録する Microsoft Azure テナント。Azure Active Directory (AD) は、アプリケーションでの認証と承認に使う ID サービスを提供します。ここでは、試用版サブスクリプションを取得できます。 [Microsoft Azure](https://account.windowsazure.com/SignUp)。

    > 重要: Azure サブスクリプションが Office 365 テナントにバインドされていることを確認する必要もあります。確認する方法については、Active Directory チームのブログ投稿「[複数の Windows Azure Active Directory を作成して管理する](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx)」をご覧ください。「**新しいディレクトリを追加する**」セクションで、この方法を説明しています。また、詳しくは、「[Office 365 開発環境のセットアップ](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription)」と「**Office 365 アカウントを Azure AD と関連付けて、アプリを作成して管理する**」のセクションをご覧ください。
* Azure に登録されたアプリケーションのクライアント ID、クライアント シークレット、リダイレクト URI の値。このサンプル アプリケーションには、**サインインしているユーザーとしてメールを送信する**アクセス許可と、**Microsoft Graph** アプリケーションの**サインインしているユーザーとしてメールを送信する**アクセス許可を付与する必要があります。[Azure に Web サーバー アプリケーションを追加](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp)し、[適切なアクセス許可を付与](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure)します。

     > メモ: アプリ登録プロセス時に、****サインオン URL** として http://127.0.0.1:8000/connect/get_token/**を必ず指定します。

## アプリの構成と実行

1. 任意の IDE を使って、*接続*ディレクトリで **config.py** を開きます。
2. *ENTER_YOUR_CLIENT_ID* を登録済みの Azure アプリケーションのクライアント ID と置き換えます。
3. *ENTER_YOUR_SECRET* を、Microsoft Azure 管理ポータルにあるアプリの **[設定]** ページで生成されたキーと置き換えます。
4. [要求: HTTP for Humans モジュール](http://docs.python-requests.org/en/latest/)を ```pip install requests``` を実行することにより、インストールします。
5. ```python manage.py migrate``` を実行してサーバーをセットアップします。[このコマンド](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate)は、データベースの状態を移行の現在のセットと同期します。
6. ```python manage.py runserver``` を実行して開発サーバーを起動します。
7. Web ブラウザーで ```http://127.0.0.1:8000/``` に移動します。

サンプルについて詳しくは、「[graph.microsoft.io の Python に関するチュートリアル](http://graph.microsoft.io/docs/platform/python)」をご覧ください。

## 質問とコメント

Office 365 Python Connect サンプルに関するフィードバックをお寄せください。質問や提案につきましては、このリポジトリの「[問題](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues)」セクションで送信できます。

お客様からのフィードバックを重視しています。[スタック オーバーフロー](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph)でご連絡ください。質問には [MicrosoftGraph] と [office365] でタグ付けしてください。
  
## その他の技術情報

* [Office デベロッパー センター](http://dev.office.com/)
* [Microsoft Graph API](http://graph.microsoft.io)
* [Office UI Fabric](http://dev.office.com/fabric)

## 著作権
Copyright (c) 2015 Microsoft.All rights reserved.
