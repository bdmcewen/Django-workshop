from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import SlideDeck


# Run the slide show
class SlideShow(TemplateView):
    template_name = "slide_show.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        slides = SlideDeck.objects.get(pk=pk)
        return {'title': slides.title, 'slideshow': slides.text}


# Show the list of notes
class SlidesList(ListView):
    model = SlideDeck
    template_name = 'slides_list.html'
