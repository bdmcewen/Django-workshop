from django.shortcuts import render


# Home View
def home(request):
    return render(request, "home.html")

# Test page
def test(request):
    return render(request, "test.html")

# Notes page
def notes(request):
    return render(request, "notes.html")

