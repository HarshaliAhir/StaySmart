# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HotelBooking.settings")  # <- Ensure this line is correct
application = get_wsgi_application()
