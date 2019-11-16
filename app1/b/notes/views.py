from django.http import HttpResponse


# HTML code to display
html_home = '''<h1>App 1b - Home</h1>
<p>
    This is simple Django app that was created using the default command script.
</p>
<p>
    This page will be shown for all requests to this server. 
</p>
<ul>
    <li>
        <a href="/">Visit Home</a>
    </li>
    <li>
        <a href="test">Visit Test</a>
    </li>
    <li>
        <a href="random">Visit Random Page</a>
    </li>
</ul>
'''

# HTML code to display
html_test = '''<h1>App 1b - Test</h1>
<p>
    This is simple Django app that was created using the default command script.
</p>
<p>
    This page will be shown for all requests to this server.
</p>
<ul>
    <li>
        <a href="/">Visit Home</a>
    </li>
    <li>
        <a href="test">Visit Test</a>
    </li>
    <li>
        <a href="random">Visit Random Page</a>
    </li>
</ul>
'''


# Home View
def home(request):
    return HttpResponse(html_home)

# Test page
def test(request):
    return HttpResponse(html_test)

