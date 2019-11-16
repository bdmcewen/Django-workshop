from django.shortcuts import render


def home(request):
    title = "App 2b - Variable Insertion - Home"
    body = 'Body Text'
    data = {'title': title, 'body': body}
    return render(request, "home.html", data)


def page1(request):
    title = "App 2b - Variable Insertion - Page 1"
    body = 'Text is injected into the template by the view code.'
    data = {'title': title, 'body': body}
    return render(request, "page.html", data)


def page2(request):
    title = "App 2b - Variable Insertion - Page 2"
    body = 'Text is injected into the template by the view code.' + \
            'This page also adds a list of items.'
    data = {'title': title, 'body': body, 'list': ['milk', 'bread', 'meat']}
    return render(request, "page.html", data)

