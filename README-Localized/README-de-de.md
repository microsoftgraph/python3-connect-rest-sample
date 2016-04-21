# Office 365 Python Connect-Beispiel unter Verwendung von Microsoft Graph

Für die Arbeit mit Office 365-Diensten und -Daten muss jede App zunächst eine Verbindung zu Office 365 herstellen. In diesem Beispiel wird gezeigt, wie die Verbindung zur und dann der Aufruf einer API über die Microsoft Graph-API (wurde zuvor als vereinheitlichte Office 365-API bezeichnet) erfolgt. Ferner wird darin die Office Fabric-Benutzeroberfläche zum Erstellen einer Office 365-Erfahrung verwendet.

> Hinweis: Rufen Sie die Seite [Erste Schritte mit Office 365-APIs](http://dev.office.com/getting-started/office365apis?platform=option-python#setup) auf. Auf dieser wird die Registrierung vereinfacht, damit Sie dieses Beispiel schneller ausführen können.

![Office 365 Python Connect-Beispielscreenshot](./README assets/screenshot.PNG)

## Voraussetzungen

Zum Verwenden des Office 365 Python Connect-Beispiels benötigen Sie Folgendes: 
* [Python 3.4.3](https://www.python.org/downloads/) 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* Ein Office 365-Konto. Sie können sich für [ein Office 365-Entwicklerabonnement](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0) registrieren. Dieses umfasst die Ressourcen, die Sie zum Erstellen von Office 365-Apps benötigen.

     > Hinweis: Wenn Sie bereits über ein Abonnement verfügen, gelangen Sie über den vorherigen Link zu einer Seite mit der Meldung *Leider können Sie Ihrem aktuellen Konto diesen Inhalt nicht hinzufügen*. Verwenden Sie in diesem Fall ein Konto aus Ihrem aktuellen Office 365-Abonnement.
* Ein Microsoft Azure-Mandant zum Registrieren Ihrer Anwendung. Von Azure Active Directory (AD) werden Identitätsdienste bereitgestellt, die durch Anwendungen für die Authentifizierung und Autorisierung verwendet werden. Hier kann ein Testabonnement erworben werden: [Microsoft Azure](https://account.windowsazure.com/SignUp).

    > Wichtig: Sie müssen zudem sicherstellen, dass Ihr Azure-Abonnement an Ihren Office 365-Mandanten gebunden ist. Rufen Sie dafür den Blogpost [Creating and Managing Multiple Windows Azure Active Directories](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx) des Active Directory-Teams auf. Im Abschnitt **Adding a new directory** finden Sie Informationen über die entsprechende Vorgehensweise. Weitere Informationen finden Sie zudem unter [Einrichten Ihrer Office 365-Entwicklungsumgebung](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription) im Abschnitt **Verknüpfen Ihres Office 365-Kontos mit Azure AD zum Erstellen und Verwalten von Apps**.
* Eine Client-ID, ein Clientgeheimnis und Umleitungs-URI-Werte einer in Azure registrierten Anwendung. Dieser Beispielanwendung müssen die Berechtigungen **Senden von E-Mails als angemeldeter Benutzer** und **Senden von E-Mails als angemeldeter Benutzer** für die **Microsoft Graph**-Anwendung gewährt werden. [Fügen Sie eine Webserveranwendung in Azure hinzu](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp), und [gewähren Sie ihr die entsprechenden Berechtigungen](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure).

     > Hinweis: Stellen Sie während des App-Registrierungsvorgangs sicher, dass Sie **http://127.0.0.1:8000/connect/get_token/** als die **Anmelde-URL**. angeben.

## Konfigurieren und Ausführen der App

1. Öffnen Sie unter Verwendung Ihrer bevorzugten IDE die Datei **config.py** im Verzeichnis *connect*.
2. Ersetzen Sie *IHRE_CLIENT_ID_EINGEBEN* durch die Client-ID Ihrer registrierten Azure-Anwendung.
3. Ersetzen Sie *IHR_GEHEIMNIS_EINGEBEN* durch einen auf der Seite für das Konfigurieren Ihrer App im Microsoft Azure-Verwaltungsportal generierten Schlüssel.
4. Installieren Sie [Requests: HTTP für menschliche Wesen](http://docs.python-requests.org/en/latest/) über die Befehlszeile, indem Sie ```pip install requests``` ausführen.
5. Richten Sie den Server durch Ausführen von ```python manage.py migrate``` ein. Mithilfe [dieses Befehls](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) wird der Datenbankstatus mit dem aktuellen Satz an Migrationen synchronisiert.
6. Starten Sie den Entwicklungsserver, indem Sie ```python manage.py runserver``` ausführen.
7. Navigieren Sie zu ```http://127.0.0.1:8000/``` im Webbrowser.

Weitere Informationen über das Beispiel finden Sie unter [Aufrufen von Microsoft Graph in einer Python-App](http://graph.microsoft.io/docs/platform/python).

## Fragen und Kommentare

Wir schätzen Ihr Feedback hinsichtlich des Office 365 Python Connect-Beispiels. Sie können uns Ihre Fragen und Vorschläge über den Abschnitt [Probleme](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues) dieses Repositorys senden.

Ihr Feedback ist uns wichtig. Nehmen Sie unter [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph) Kontakt mit uns auf. Taggen Sie Ihre Fragen mit [MicrosoftGraph] und [office365].
  
## Zusätzliche Ressourcen

* [Office Dev Center](http://dev.office.com/)
* [Microsoft Graph-API](http://graph.microsoft.io)
* [Office-UI-Fabric](http://dev.office.com/fabric)

## Copyright
Copyright (c) 2015 Microsoft. Alle Rechte vorbehalten.
