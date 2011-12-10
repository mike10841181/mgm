

import os
import sys

sys.path.append('/home/mikeandinog/workspace')
sys.path.append('/home/mikeandinog/workspace/mgm')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mgm.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
