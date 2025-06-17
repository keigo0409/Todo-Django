import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

django.setup()

from django.core.management import call_command
from django.db import OperationalError

try:
    call_command("migrate", interactive=False)
except OperationalError as e:
    print("Database not ready yet:", e)
