from django.conf.urls import url
from django.http import HttpResponse


# HTML code to display
html = '''<h1>App 1a - Simple App</h1>
<p>
    This is simple Django app that was created using the default command script.
</p>
<p>
    This page will be shown for all requests to this server.
</p>
'''


# Home View
def home(request):
    return HttpResponse(html)

# Test page
def test(request):
    return HttpResponse("<h1>App 1a - Test page</h1><a href=x>home</a>")


# URL patterns to match
urlpatterns = [
    url('test', test),
    url('', home),
]


