# Exemplo de conexão com o Office 365 para Python usando o Microsoft Graph

A primeira etapa para que os aplicativos comecem a funcionar com dados e serviços do Office 365 é estabelecer uma conexão com essa plataforma. Este exemplo mostra como se conectar e chamar uma única API através da API do Microsoft Graph (antiga API unificada do Office 365) e usa o Office Fabric UI para criar uma experiência do Office 365.

> Observação: experimente a página [Introdução às APIs do Office 365](http://dev.office.com/getting-started/office365apis?platform=option-python#setup), que simplifica o registro para que você possa executar esse exemplo com mais rapidez.

![Captura de tela do exemplo de conexão com o Office 365 para Python](../README assets/screenshot.png)

## Pré-requisitos

Para usar o exemplo de conexão com o Office 365 para Python, é necessário o seguinte: 
* [Python 3.4.3](https://www.python.org/downloads/) 
* [Django 1.8](https://docs.djangoproject.com/en/1.8/intro/install/) 
* Uma conta do Office 365. Inscreva-se para [uma Assinatura de Desenvolvedor do Office 365](https://portal.office.com/Signup/Signup.aspx?OfferId=6881A1CB-F4EB-4db3-9F18-388898DAF510&DL=DEVELOPERPACK&ali=1#0), que inclui os recursos necessários para começar a criação de aplicativos do Office 365.

     > Observação: caso já tenha uma assinatura, o link anterior direciona você para uma página com a mensagem *Não é possível adicioná-la à sua conta atual*. Nesse caso, use uma conta de sua assinatura atual do Office 365.
* Um locatário do Microsoft Azure para registrar o seu aplicativo. O Active Directory (AD) do Azure fornece serviços de identidade que os aplicativos usam para autenticação e autorização. Você pode adquirir uma assinatura de avaliação aqui: [Microsoft Azure](https://account.windowsazure.com/SignUp).

    > Importante: você também deve assegurar que a sua assinatura do Azure esteja vinculada ao seu locatário do Office 365. Para saber como fazer isso, confira a postagem de blog da equipe do Active Directory, [Criando e gerenciando vários Active Directories do Microsoft Azure](http://blogs.technet.com/b/ad/archive/2013/11/08/creating-and-managing-multiple-windows-azure-active-directories.aspx). A seção **Adicionando um novo diretório** explica como fazer isso. Para saber mais, confira o artigo [Configurar o ambiente de desenvolvimento do Office 365](https://msdn.microsoft.com/office/office365/howto/setup-development-environment#bk_CreateAzureSubscription) e a seção **Associar uma conta do Office 365 ao AD do Azure para criar e gerenciar aplicativos**.
* Valores de uma ID do cliente, do segredo do cliente e do URI de redirecionamento de um aplicativo registrado no Azure. Esse exemplo de aplicativo deve ter as permissões **Enviar email como usuário conectado** e **Enviar email como usuário conectado** concedidas para o aplicativo **Microsoft Graph**. Para isso, [adicione um servidor Web no Microsoft Azure](https://msdn.microsoft.com/office/office365/HowTo/add-common-consent-manually#bk_RegisterServerApp) e [conceda as permissões adequadas](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/wiki/Grant-permissions-to-the-Connect-application-in-Azure).

     > Observação: durante o processo de registro do aplicativo, não deixe de especificar **http://127.0.0.1:8000/connect/get_token/** como a **URL de Entrada**.

## Configurar e executar o aplicativo

1. Abra **config.py** no diretório *Conexão* usando seu IDE favorito.
2. Substitua *ENTER_YOUR_CLIENT_ID* pela ID do cliente do aplicativo Azure registrado.
3. Substitua *ENTER_YOUR_SECRET* por uma chave gerada na página **Configurar** do aplicativo, no Portal de Gerenciamento do Microsoft Azure.
4. Instale o módulo da biblioteca [Requests: HTTP para Humanos](http://docs.python-requests.org/en/latest/) na linha de comando, executando ```pip install requests```.
5. Configure o servidor executando ```python manage.py migrate```. [Este comando](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-migrate) vai sincronizar o estado do banco de dados com o conjunto de migrações atual.
6. Inicie o servidor de desenvolvimento executando ```python manage.py runserver```.
7. Acesse ```http://127.0.0.1:8000/``` no navegador da Web.

Para saber mais sobre o exemplo, confira o artigo [Explicação passo a passo sobre o Python em graph.microsoft.io](http://graph.microsoft.io/docs/platform/python).

## Perguntas e comentários

Gostaríamos de saber sua opinião sobre o exemplo de conexão com o Office 365 para Python. Você pode enviar perguntas e sugestões na seção [Problemas](https://github.com/OfficeDev/O365-Python-Microsoft-Graph-Connect/issues) deste repositório.

Os seus comentários são importantes para nós. Junte-se a nós na página do [Stack Overflow](http://stackoverflow.com/questions/tagged/office365+or+microsoftgraph). Marque as suas perguntas com [MicrosoftGraph] e [office365].
  
## Recursos adicionais

* [Centro de Desenvolvimento do Office](http://dev.office.com/)
* [API do Microsoft Graph](http://graph.microsoft.io)
* [Office UI Fabric](http://dev.office.com/fabric)

## Direitos autorais
Copyright © 2015 Microsoft. Todos os direitos reservados.
