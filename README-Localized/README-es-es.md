# Ejemplo Connect de Python para Office 365 con Microsoft Graph

Conectarse a Office 365 es el primer paso que debe realizar cada aplicación para empezar a trabajar con los datos y servicios de Office 365. Este ejemplo muestra cómo conectar y cómo llamar después a una API mediante la API de Microsoft Graph (anteriormente denominada API unificada de Office 365), y usa la interfaz de usuario Fabric de Office para crear una experiencia de Office 365.

> Nota: Consulte [Introducción a las API de Office 365](http://dev.office.com/getting-started/office365apis?platform=option-python#setup), que simplifica el registro para que este ejemplo se ejecute más rápidamente.

![Captura de pantalla del ejemplo Connect de Python para Office 365](./README assets/screenshot.PNG)

## Requisitos previos

Para usar el ejemplo Connect de Python para Office 365, necesita lo siguiente: 
* [Python 3.4.3](https://www.python.org/downloads/) 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* Una cuenta de Office 365. Puede registrarse en [una suscripción a Office 365 Developer](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0), que incluye los recursos que necesita para comenzar a crear aplicaciones de Office 365.

     > Nota: Si ya dispone de una suscripción, el vínculo anterior le dirige a una página con el mensaje *No se puede agregar a su cuenta actual*. En ese caso, use una cuenta de su suscripción actual a Office 365
* Un inquilino de Microsoft Azure para registrar la aplicación. Azure Active Directory (AD) proporciona servicios de identidad que las aplicaciones usan para autenticación y autorización. Puede adquirir una suscripción de prueba aquí: [Microsoft Azure](https://account.windowsazure.com/SignUp).

    > Importante: También necesita asegurarse de que su suscripción a Azure está enlazada a su inquilino de Office 365. Para ello, consulte la publicación del blog del equipo de Active Directory, [Crear y administrar varios directorios de Windows Azure Active Directory](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx). La sección **Agregar un nuevo directorio** le explicará cómo hacerlo. Para obtener más información, también puede consultar [Configurar el entorno de desarrollo de Office 365](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription) y la sección **Asociar su cuenta de Office 365 con Azure AD para crear y administrar aplicaciones**.
* Los valores de identificador de cliente, secreto de cliente y URI de redireccionamiento de una aplicación registrada en Azure. A esta aplicación de ejemplo se le debe conceder el permiso **Enviar correo como usuario con sesión iniciada** para la aplicación de **Microsoft Graph**. [Agregar una aplicación de servidor web en Azure](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp) y [concederle los permisos adecuados](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure).

     > Nota: Durante el proceso de registro de la aplicación, asegúrese de especificar **http://127.0.0.1:8000/connect/get_token/** como **Dirección URL de inicio de sesión**.

## Configurar y ejecutar la aplicación

1. Con su IDE favorito, abra **config.py** en el directorio *connect*.
2. Reemplace *ENTER_YOUR_CLIENT_ID* por el identificador de cliente de la aplicación registrada en Azure.
3. Reemplace *ENTER_YOUR_SECRET* por una clave generada en la página **Configurar** de la aplicación en el Portal de administración de Microsoft Azure.
4. Instale el [módulo HTTP for Humans de Requests](http://docs.python-requests.org/en/latest/) desde la línea de comandos mediante la ejecución de ```pip install requests```.
5. Configure el servidor mediante la ejecución de ```python manage.py migrate```. [Este comando](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) sincronizará el estado de la base de datos con el conjunto actual de migraciones.
6. Inicie el servidor de desarrollo mediante la ejecución de ```python manage.py runserver```.
7. Vaya a ```http://127.0.0.1:8000/``` en el explorador web.

Para obtener más información sobre el ejemplo, consulte [Tutorial de Python en graph.microsoft.io](http://graph.microsoft.io/docs/platform/python).

## Preguntas y comentarios

Nos encantaría recibir sus comentarios acerca del ejemplo Connect de Python para Office 365. Puede enviarnos sus preguntas y sugerencias a través de la sección [Problemas](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues) de este repositorio.

Su opinión es importante para nosotros. Conecte con nosotros en [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph). Etiquete sus preguntas con [MicrosoftGraph] y [office365].
  
## Recursos adicionales

* [Centro para desarrolladores de Office](http://dev.office.com/)
* [API de Microsoft Graph](http://graph.microsoft.io)
* [Interfaz de usuario Fabric de Office](http://dev.office.com/fabric)

## Copyright
Copyright (c) 2015 Microsoft. Todos los derechos reservados.
