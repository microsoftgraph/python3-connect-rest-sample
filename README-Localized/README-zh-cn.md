# 使用 Microsoft Graph 的 Office 365 Python Connect 示例

连接到 Office 365 是每个应用开始使用 Office 365 服务和数据必须采取的第一步。该示例演示如何通过 Microsoft Graph API（旧称 Office 365 统一 API）连接并调用 API，以及如何使用 Office 结构 UI 创建 Office 365 体验。

> 注意： 尝试 [Office 365 API 入门](http://dev.office.com/getting-started/office365apis?platform=option-python#setup)页面，其简化了注册，使您可以更快地运行该示例。

![Office 365 Python Connect 示例屏幕截图](./README assets/screenshot.PNG)

## 先决条件

要使用 Office 365 Python Connect 示例，您需要满足以下条件： 
* [Python 3.4.3](https://www.python.org/downloads/) 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* 拥有一个 Office 365 帐户。您可以注册 [Office 365 开发人员订阅](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0)，其中包含您开始构建 Office 365 应用所需的资源。

     > 注意： 如果您已经订阅，之前的链接会将您转至包含以下信息的页面：*抱歉，您无法将其添加到当前帐户*。在这种情况下，请使用当前 Office 365 订阅中的帐户。
* 用于注册您的应用程序的 Microsoft Azure 租户。Azure Active Directory (AD) 为应用程序提供了用于进行身份验证和授权的标识服务。您还可在此处获得试用订阅： [Microsoft Azure](https://account.windowsazure.com/SignUp)。

    > 重要说明： 您还需要确保您的 Azure 订阅已绑定到 Office 365 租户。要执行这一操作，请参阅 Active Directory 团队的博客文章：[创建和管理多个 Microsoft Azure Active Directory](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx)。**添加新目录**一节将介绍如何执行此操作。您还可以参阅[设置 Office 365 开发环境](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription)和**关联您的 Office 365 帐户和 Azure AD 以创建并管理应用**一节获取详细信息。
* 在 Azure 中注册的应用程序的客户端 ID、客户端密码和重定向 URI 值。必须向该示例应用程序授予**以登录用户身份发送邮件**和**以登录用户身份发送邮件**权限以使用 **Microsoft Graph** 应用程序。[在 Azure 中添加 Web 服务器应用程序](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp)并向其[授予适当的权限](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure)。

     > 注意： 在应用注册过程中，务必指定 **http://127.0.0.1:8000/connect/get_token/** 作为**登录 URL**。

## 配置并运行应用

1. 使用您最喜爱的 IDE 打开 *连接*目录中的 **config.py**。
2. 用所注册的 Azure 应用程序的客户端 ID 替换 *ENTER_YOUR_CLIENT_ID*。
3. 用 Microsoft Azure 管理门户中应用的**配置**页面生成的密钥替换 *ENTER_YOUR_SECRET*。
4. 通过运行以下代码从命令行安装 [请求： HTTP for Humans 模块](http://docs.python-requests.org/en/latest/)：```pip install requests```。
5. 通过运行 ```python manage.py migrate``` 设置服务器。[此命令](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate)将同步数据库状态和当前迁移组。
6. 通过运行 ```python manage.py runserver``` 启动开发服务器。
7. 导航到 Web 浏览器中的 ```http://127.0.0.1:8000/```。

若要了解有关该示例的详细信息，请参阅 [graph.microsoft.io 上的 Python 演练](http://graph.microsoft.io/docs/platform/python)。

## 问题和意见

我们乐意倾听您有关 Office 365 Python Connect 示例的反馈。您可以在该存储库中的[问题](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues)部分将问题和建议发送给我们。

您的反馈对我们意义重大。请在[堆栈溢出](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph)上与我们联系。使用 [MicrosoftGraph] 和 [office365] 标记出您的问题。
  
## 其他资源

* [Office 开发人员中心](http://dev.office.com/)
* [Microsoft Graph API](http://graph.microsoft.io)
*[Office UI 结构](http://dev.office.com/fabric)

## 版权所有
版权所有 (c) 2015 Microsoft。保留所有权利。
