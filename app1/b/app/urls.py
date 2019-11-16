from django.conf.urls import url
from notes.views import home, test



# URL patterns to match
urlpatterns = [
    url('test', test),
    url('', home),
]


