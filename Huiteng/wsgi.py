"""
WSGI config for Huiteng project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys
print(sys.prefix)
# add the hellodjango project path into the sys.path
sys.path.append('/home/wangwei/projects/HuiTeng/Huiteng')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/root/.virtualenvs/huitengenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Huiteng.settings")

application = get_wsgi_application()
