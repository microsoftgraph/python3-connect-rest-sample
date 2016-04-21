# Exemple de connexion de Python à Office 365 avec Microsoft Graph

La connexion à Office 365 est la première étape que chaque application doit suivre pour commencer à travailler avec les données et services Office 365. Cet exemple explique comment connecter, puis appeler une API via l’API Microsoft Graph (anciennement appelée API unifiée Office 365). Il utilise la structure d’interface utilisateur d’Office pour créer une expérience Office 365.

> Remarque : consultez la page relative à la [prise en main des API Office 365](http://dev.office.com/getting-started/office365apis?platform=option-python#setup) pour enregistrer plus facilement votre application et exécuter plus rapidement cet exemple.

![Capture d’écran d’un exemple de connexion de Python à Office 365](./README assets/screenshot.PNG)

## Conditions préalables

Pour utiliser l’exemple de connexion de Python à Office 365, vous devez disposer des éléments suivants : 
* [Python 3.4.3](https://www.python.org/downloads/) 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* Un compte Office 365. Vous pouvez vous inscrire à [Office 365 Developer](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0) pour accéder aux ressources dont vous avez besoin pour commencer à créer des applications Office 365.

     > Remarque : si vous avez déjà un abonnement, le lien précédent vous renvoie vers une page avec le message suivant : *Désolé, vous ne pouvez pas ajouter ceci à votre compte existant*. Dans ce cas, utilisez un compte lié à votre abonnement Office 365 existant.
* Un client Microsoft Azure pour enregistrer votre application. Azure Active Directory (AD) fournit des services d’identité que les applications utilisent à des fins d’authentification et d’autorisation. Un abonnement d’évaluation peut être demandé ici : [Microsoft Azure](https://account.windowsazure.com/SignUp).

    > Important : vous devez également vous assurer que votre abonnement Azure est lié à votre client Office 365. Pour cela, consultez le billet du blog de l’équipe d’Active Directory relatif à la [création et la gestion de plusieurs fenêtres dans les répertoires Azure Active Directory](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx). La section sur l’**ajout d’un nouveau répertoire** vous explique comment procéder. Pour en savoir plus, vous pouvez également consulter la rubrique relative à la [configuration de votre environnement de développement Office 365](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription) et la section sur l’**association de votre compte Office 365 à Azure Active Directory pour créer et gérer des applications**.
* Un ID client, une clé secrète client et les valeurs URI de redirection d’une application enregistrée dans Azure. Cet exemple d’application doit obtenir l’autorisation **Envoyer du courrier en tant qu’utilisateur connecté** pour l’application **Microsoft Graph**. [Ajoutez une application de serveur web dans Azure](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp) et [accordez-lui les autorisations appropriées](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure).

     > Remarque : pendant l’enregistrement de l’application, veillez à sélectionner **http://127.0.0.1:8000/connect/get_token/** comme **URL d’authentification**.

## Configuration et exécution de l’application

1. À l’aide de votre IDE favori, ouvrez **config.py** dans le répertoire *connect*.
2. Remplacez *ENTER_YOUR_CLIENT_ID* par l’ID client de votre application Azure enregistrée.
3. Remplacez *ENTER_YOUR_SECRET* par une clé générée sur la page **Configurer** de votre application dans le portail de gestion Microsoft Azure.
4. Installez le module [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/) depuis la ligne de commande en exécutant ```pip install requests```.
5. Configurez le serveur en exécutant ```python manage.py migrate```. [Cette commande](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) synchronisera l’état de la base de données avec l’ensemble de migrations en cours.
6. Démarrez le serveur de développement en exécutant ```python manage.py runserver```.
7. Accédez à ```http://127.0.0.1:8000/``` dans votre navigateur web.

Pour en savoir plus sur cet exemple, consultez la [procédure pas à pas de l’exécution de Python sur graph.microsoft.io](http://graph.microsoft.io/docs/platform/python).

## Questions et commentaires

Nous serions ravis de connaître votre opinion sur l’exemple de connexion de Python à Office 365. Vous pouvez nous faire part de vos questions et suggestions dans la rubrique [Problèmes](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues) de ce référentiel.

Votre avis compte beaucoup pour nous. Communiquez avec nous sur [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph). Posez vos questions avec les tags [MicrosoftGraph] et [Office 365].
  
## Ressources supplémentaires

* [Centre de développement Office](http://dev.office.com/)
* [API Microsoft Graph](http://graph.microsoft.io)
* [Structure d’interface utilisateur d’Office](http://dev.office.com/fabric)

## Copyright
Copyright (c) 2015 Microsoft. Tous droits réservés.
