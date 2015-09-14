"""
WSGI config for O365_Python_Unified_API_Connect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "O365_Python_Unified_API_Connect.settings")

application = get_wsgi_application()
