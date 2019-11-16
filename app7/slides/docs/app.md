# Building a Presentation App

* Step by Step (in 20 minutes)
* by Mark Seaman

![](/static/Bear.png)


### Software Lifecycle
* Requirements
* Design
* Code
* Test


## Requirements
* Apps = Data + Views
* Data
    * Database - SQL Lite
    * SlideDeck - Database table records
        * title - for presentation
        * text - content of slide deck
* Views
    * List of presentations
    * Use admin view to create presentation
    * Run selected presentation



## Design

### Slide Show Data Records
* SlideDeck show records 
    * id (primary key for table)
    * title (100 characters) - for presentation
    * text (Text Area for unlimited text)- content of slide deck
    

### Slide Show Views
* List of slide shows
* Run the presentation
    * Use Reveal JS to show slides
    * Run slides in new browser tab
* Add new show - admin view 
* Edit existing show - admin view 
* Delete a show - admin view 



## Code

### SlideDeck
* Display list of slides

models.py

```python
from django.db import models

class SlideDeck (models.Model):
    title = models.CharField (max_length=100)
    text = models.TextField ()
```


### SlidesList
* Display list of slides

views.py

```python
from django.views.generic import ListView
from .models import SlideDeck

class SlidesList(ListView):
    model = SlideDeck
    template_name = 'slides_list.html'
```


### SlidesList
* Display list of slides

templates/slides_list.html

```html
<ul>
    {% for slides in object_list %}
        <li>
            <a href="{{ slides.pk }}/">
                {{ slides.title }}
            </a>
        </li>
    {% endfor %}
</ul>
```


### SlideShow
* Display the slide show

views.py

```python
from django.views.generic import TemplateView
from .models import SlideDeck

class SlideShow(TemplateView):
    template_name = "reveal.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        slides = SlideDeck.objects.get(pk=pk)
        return {'title': slides.title, 'slideshow': slides.text}
```


### SlideShow
* Display the slide show

templates/slides_show.html

```html

<!DOCTYPE html>
<html>

<head>
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://revealjs.com/css/reveal.css">
    <link rel="stylesheet" href="https://revealjs.com/css/theme/white.css">
    <link rel="stylesheet" href="https://revealjs.com/lib/css/zenburn.css" />
    <link rel="stylesheet" href="/static/slides.css">
</head>

<body>

    <div class="reveal">
        <div class="slides">
            <!--     data-separator="\n---\n" data-separator-vertical="\n--\n"       -->
            <section data-markdown data-separator="\n## " data-separator-vertical="\n### ">
                <textarea data-template>
                {{ slideshow }}
                </textarea>
            </section>
        </div>
    </div>

    <script src="https://revealjs.com/lib/js/head.min.js"></script>
    <script src="https://revealjs.com/js/reveal.js"></script>
    <script src="/static/slides.js"></script>

</body>

</html>
```


## Test

### Basic Usability Test
* Start up web server
* Display page at "localhost:8005/slides"
* Run slide show 
* Add new slide show
* Test new presentation



![](/static/Bear.png)

