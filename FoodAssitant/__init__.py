import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FoodAssitant.settings")
django.setup()
from FoodAssitant.models import *