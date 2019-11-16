from django.contrib import admin
from django.urls import path

from notes.views import Notes, NoteCreate, NoteDelete, NoteList, NoteUpdate
from slides.views import SlidesList, SlideShow


urlpatterns = [
    
    # User Admin
    path('admin/', admin.site.urls),
    
    # Slide Show
    path('slides/<int:pk>', SlideShow.as_view()),
    
    # List View
    path('slides/', SlidesList.as_view(), name='slides-list'),
    
    # Add View
    path('add', NoteCreate.as_view(), name='note-add'),
    
    # Edit View
    path('<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    
    # Delete View
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),
    
    # List View
    path('', NoteList.as_view(), name='note-list'),

]

