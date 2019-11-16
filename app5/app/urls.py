from django.conf.urls import url
from django.urls import path

from notes.views import Notes, NoteCreate, NoteDelete, NoteList, NoteUpdate


urlpatterns = [
    
    # Add View
    path('add', NoteCreate.as_view(), name='note-add'),
    
    # Edit View
    path('<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    
    # Delete View
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),
    
    # List View
    path('', NoteList.as_view(), name='note-list'),

]

