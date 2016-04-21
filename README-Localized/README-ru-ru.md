# Пример приложения на Python, подключающегося к Office 365 и использующего Microsoft Graph

Подключение к Office 365 — это первый шаг, который должно выполнить каждое приложение, чтобы начать работу со службами и данными Office 365. В этом примере показано, как подключить и вызвать один API с помощью API Microsoft Graph (прежнее название — единый API Office 365), а также использовать платформу Office UI Fabric для работы с Office 365.

> Примечание. Перейдите на страницу [Начало работы с API Office 365](http://dev.office.com/getting-started/office365apis?platform=option-python#setup) для упрощенной регистрации, чтобы ускорить запуск этого примера.

![Снимок экрана с примером приложения на Python, подключающегося к Office 365] (../README assets/screenshot.PNG)

## Предварительные требования

Чтобы воспользоваться примером приложения на Python, подключающегося к Office 365, требуются перечисленные ниже компоненты. 
* [Python 3.4.3](https://www.python.org/downloads/). 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/). 
* Учетная запись Office 365. Вы можете [подписаться на план Office 365 для разработчиков](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0), включающий ресурсы, которые необходимы для создания приложений Office 365.

     > Примечание. Если у вас уже есть подписка, при выборе приведенной выше ссылки откроется страница с сообщением *К сожалению, вы не можете добавить это к своей учетной записи*. В этом случае используйте учетную запись, сопоставленную с текущей подпиской на Office 365.
* Клиент Microsoft Azure для регистрации приложения. В Azure Active Directory (AD) доступны службы идентификации, которые приложения используют для проверки подлинности и авторизации. Здесь можно получить пробную подписку: [Microsoft Azure](https://account.windowsazure.com/SignUp).

    > Внимание! Убедитесь, что ваша подписка на Azure привязана к клиенту Office 365. Для этого просмотрите запись в блоге команды Active Directory, посвященную [созданию нескольких каталогов Microsoft Azure AD и управлению ими](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx). Инструкции приведены в разделе о **добавлении нового каталога**. Дополнительные сведения см. в статье [Как настроить среду разработки для Office 365](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription) и, в частности, в разделе **Связывание Azure AD и учетной записи Office 365 для создания приложений и управления ими**.
* Универсальный код ресурса (URI) для перенаправления, секрет клиента и идентификатор клиента, указанные при регистрации приложения в Azure. Этому примеру приложения необходимо предоставить разрешения **Отправка почты от имени вошедшего пользователя** и **Отправка почты от имени вошедшего пользователя** для приложения, использующего **Microsoft Graph**. [Добавьте приложение веб-сервера в Azure](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp) и [предоставьте ему необходимые разрешения](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure).

     > Примечание. При регистрации приложения укажите **http://127.0.0.1:8000/connect/get_token/** как значение параметра **URL-адрес входа**.

## Настройка и запуск приложения

1. С помощью выбранного интерфейса IDE откройте файл **config.py** в каталоге *connect*.
2. Замените *ENTER_YOUR_CLIENT_ID* на идентификатор клиента для зарегистрированного в Azure приложения.
3. Замените *ENTER_YOUR_SECRET* на ключ приложения, созданный на странице **Настройка** на портале управления Microsoft Azure.
4. Установите модуль [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/) из командной строки, выполнив команду ```pip install requests```.
5. Настройте сервер, выполнив команду ```python manage.py migrate```. [Эта команда](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) синхронизирует состояние базы данных с текущим набором миграций.
6. Запустите сервер разработки, выполнив команду ```python manage.py runserver```.
7. Введите адрес ```http://127.0.0.1:8000/``` в веб-браузере.

Дополнительные сведения о приложении см. в [пошаговых инструкциях касательно Python на сайте graph.microsoft.io](http://graph.microsoft.io/docs/platform/python).

## Вопросы и комментарии

Мы будем рады получить от вас отзывы о примере приложения на Python, подключающегося к Office 365. Отправляйте нам свои вопросы и предложения в раздел этого репозитория, посвященный [проблемам](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues).

Ваши отзывы важны для нас. Для связи с нами используйте сайт [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph). Помечайте свои вопросы тегами [MicrosoftGraph] и [office365].
  
## Дополнительные ресурсы

* [Центр разработки для Office](http://dev.office.com/)
* [API Microsoft Graph](http://graph.microsoft.io)
* [Office UI Fabric](http://dev.office.com/fabric)

## Авторские права
(c) Корпорация Майкрософт (Microsoft Corporation), 2015. Все права защищены.
