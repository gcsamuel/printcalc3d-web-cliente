import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

try:
    call_command("migrate")
except:
    pass

app = get_wsgi_application()
