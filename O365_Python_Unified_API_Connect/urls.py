"""O365_Python_Unified_API_Connect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from connect.views import home, get_token, main, send_mail, disconnect

urlpatterns = [
    # Invoke the home view in the connect app by default
    url(r'^$', home, name='home'),
    # Defer any URLS to the /connect directory to the connect app
    url(r'^$', home, name='home'),  
    url(r'^get_token/$', get_token, name='get_token'),
    url(r'^main/$', main, name='main'),
    url(r'^send_mail/$', send_mail, name='send_mail'),
    url(r'^disconnect/$', disconnect, name='disconnect'),
    url(r'^admin/', include(admin.site.urls)),
]
