from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from notes.models import Note


# Show the default view
class Notes(TemplateView):
    template_name = 'home.html'
    

# Show the list of notes
class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'
    
    
# Add one note
class NoteCreate(CreateView):
    model = Note
    template_name = 'note_add.html'
    fields = ['title', 'text']
    

# Edit a note
class NoteUpdate(UpdateView):
    model = Note
    template_name = 'note_edit.html'
    fields = ['title', 'text']
    

# Delete a note
class NoteDelete(DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note-list')

