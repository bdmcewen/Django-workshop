from django.http import HttpResponse


# Home View
def home(request):
    html = '''
        <h1>App 3 - Home</h1>
        <ul>
            <li>
                <a href="/">Top of Web Server</a>
            </li>
             <li>
                <a href="static/Bear.png">Bear.png</a> - shows static server
            </li>
            <li>
                <a href="1">Test #1</a> - pass arg in URL path
            </li>
            <li>
                <a href="2">Test #2</a> - pass arg in URL path
            </li>
            <li>
                <a href="doc/Slides.md">Slides as document</a>
            </li>
            <li>
                <a href="year/2019">Show the Year</a>
            </li>
            <li>
                <a href="doc/Slides.md">Slides as document</a>
            </li>
            <li>
                <a href="enroll?school=UNC&student=me">Query Parameter</a>
            </li>
        </ul>
        '''
    return HttpResponse(html)


# Test page
def test(request, tst_num):
    html = '<h1>App 3 - Test</h1> <p> The test you chose to run in Test #%s </p>'
    return HttpResponse(html % tst_num)


# Document page
def doc(request, title):
    html = '<h1>App 3 - Document</h1><p>Document Title = <b>%s</b></p>'
    return HttpResponse(html % title)


# Year page
def year(request, title):
    html = '<h1>App 3 - Year</h1><p>Year = <b>%s</b></p>'
    return HttpResponse(html % title)


# Enroll page
def enroll(request):
    html = '<h1>App 3 - Enroll</h1><p>School = <b>%s</b>, Student=<b>%s</b></p>'
    school = request.GET.get('school')
    student = request.GET.get('student')
    return HttpResponse(html % (school, student))

