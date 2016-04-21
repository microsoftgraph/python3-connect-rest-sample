# 使用 Microsoft Graph 的 Office 365 Python Connect 範例

連接到 Office 365 是每個應用程式要開始使用 Office 365 服務和資料時必須採取的第一個步驟。此範例示範如何透過 Microsoft Graph API (之前稱為 Office 365 統一 API) 連接而後呼叫一個 API，然後使用 Office Fabric UI 來打造 Office 365 經驗。

> 注意事項： 嘗試可簡化註冊的 [Office 365 API 入門](http://dev.office.com/getting-started/office365apis?platform=option-python#setup)頁面，以便您更快速地執行這個範例。

![Office 365 Python Connect 範例螢幕擷取畫面](../README assets/screenshot.PNG)

## 必要條件

若要使用 Office 365 Python Connect 範例，您需要下列各項：
* [Python 3.4.3](https://www.python.org/downloads/)
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* Office 365 帳戶。您可以註冊 [Office 365 開發人員訂用帳戶](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0)，其中包含開始建置 Office 365 應用程式所需的資源。

     > 注意事項： 如果您已有訂用帳戶，則先前的連結會讓您連到顯示「抱歉，您無法將之新增到您目前的帳戶」訊息的頁面。在此情況下，請使用您目前的 Office 365 訂用帳戶所提供的帳戶。
* 用來註冊您的應用程式的 Microsoft Azure 租用戶。Azure Active Directory (AD) 會提供識別服務，以便應用程式用於驗證和授權。在這裡可以取得試用版的訂用帳戶： [Microsoft Azure](https://account.windowsazure.com/SignUp)。

    > 重要事項： 您還需要確定您的 Azure 訂用帳戶已繫結至您的 Office 365 租用戶。若要執行這項操作，請參閱 Active Directory 小組的部落格文章：[建立和管理多個 Windows Azure Active Directory](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx)。**新增目錄**一節將說明如何執行這項操作。如需詳細資訊，也可以參閱[設定 Office 365 開發環境](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription)和**建立 Office 365 帳戶與 Azure AD 的關聯以便建立和管理應用程式**一節。
* 在 Azure 中註冊之應用程式的用戶端識別碼、用戶端密碼及重新導向 URI 值。此範例應用程式必須取得 **Microsoft Graph** 應用程式的 [以登入的使用者身分傳送郵件] 權限。[在 Azure 中新增 Web 伺服器應用程式](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp)和[授與適當的權限](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure)給它。

     > 注意事項： 在應用程式註冊過程中，請務必指定 **http://127.0.0.1:8000/connect/get_token/** 做為 [登入 URL]。

## 設定和執行應用程式

1. 使用您最愛的 IDE，開啟 *connect* 目錄中的 **config.py**。
2. 用已註冊之 Azure 應用程式的用戶端識別碼來取代 *ENTER_YOUR_CLIENT_ID*。
3. 用在 Microsoft Azure 管理入口網站中您應用程式的 [設定] 頁面上產生的金鑰來取代 *ENTER_YOUR_SECRET*。
4. 從命令列安裝 [Requests: HTTP for Humans 模組](http://docs.python-requests.org/en/latest/)，方法是執行 ```pip install requests```。
5. 執行 ```python manage.py migrate``` 以設定伺服器。[這個命令](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate)將同步處理資料庫狀態與目前的移轉集。
6. 執行 ```python manage.py runserver``` 以啟動開發伺服器。
7. 在網頁瀏覽器中瀏覽至 ```http://127.0.0.1:8000/```。

若要深入了解此範例，請參閱 [graph.microsoft.io 上的 Python 逐步解說](http://graph.microsoft.io/docs/platform/python)。

## 問題與意見

我們很樂於收到您對於 Office 365 Python Connect 範例的意見反應。您可以在此儲存機制的[問題](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues)區段中，將您的問題及建議傳送給我們。

我們很重視您的意見。請透過 [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph) 與我們連絡。以 [MicrosoftGraph] 和 [office365] 標記您的問題。
  
## 其他資源

* [Office 開發中心](http://dev.office.com/)
* [Microsoft Graph API](http://graph.microsoft.io)
* [Office UI Fabric](http://dev.office.com/fabric)

## 著作權
Copyright (c) 2015 Microsoft.著作權所有，並保留一切權利。
