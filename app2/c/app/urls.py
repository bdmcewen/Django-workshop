from django.conf.urls import url
from notes.views import home, page1, page2, page3


# URL patterns to match
urlpatterns = [
    url('page1', page1),
    url('page2', page2),
    url('page3', page3),
    url('', home),
]


