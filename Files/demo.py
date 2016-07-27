__author__ = 'vivekmalik'
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings

class StartupMiddleware(object):
    def __init__(self):
        print "Hello world"
        raise MiddlewareNotUsed('Startup complete')