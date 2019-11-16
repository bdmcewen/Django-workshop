from django.shortcuts import render


# Home View
def home(request):
    title = "App 2c - View Inheritance - Home Page"
    text = 'Body Text is injected into the page template.'
    data = dict(title=title, content=text)
    return render(request, "home.html", data)


# Test page
def page1(request):
    title = "App 2c - View Inheritance - Page 1"
    content = 'Body Text is injected into the page template.'
    data = dict(title=title, body=content)
    return render(request, "page.html", data)


# Notes page
def page2(request):
    title = "App 2c - View Inheritance - Notes Page 2"
    text = 'This information is passed from the view into the "notes.html" template.'
    data = dict(title=title, body=text)
    return render(request, "page.html", data)

# Custom page
def page3(request):
    title = "App 2c - Custom - Notes Page 3"
    text = 'CHitty Bang Bang, Chitty Chitty Bang Bang'
    data = dict(title=title, body=text)
    return render(request, "page.html", data)


# Missing page
def missing(request):
    title="Page Not Found"
    data = dict(title=title, url=request.path) 
    return render(request, "missing.html", data)


# UNC View
def unc(request):
    title = "App 2c - View Inheritance - UNC Page"
    return render(request, "unc.html", dict(title=title))
