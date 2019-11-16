# settings.py   - Build the smallest possible web app

from django.conf.urls import url
from django.http import HttpResponse

# Required Django Setup
DEBUG=True
SECRET_KEY = 'KDqYibgo1ZI4QIHOFInXmTy6wknXxWiii5DBal825FQgCXo5zA'
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'settings'
ALLOWED_HOSTS = ['*']

# Home View
def home(request):
    return HttpResponse("<h1>Simple App</h1><p>This is the simplest Django app that is possible.</p>")

# URL Route
urlpatterns = [
    url(r'^$', home),
]
