from django.urls import path
from .views import doc, enroll, home, test, year

urlpatterns = [
    path('', home),
    path('enroll', enroll),
    path(r'year/<int:title>', year),
    path('<int:tst_num>', test),
    path(r'doc/<title>', doc),
]
