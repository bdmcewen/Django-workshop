from django.conf.urls import url
from notes.views import home, notes, test



# URL patterns to match
urlpatterns = [
    url('notes', notes),
    url('test', test),
    url('', home),
]


