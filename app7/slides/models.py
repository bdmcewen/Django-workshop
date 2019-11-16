from django.db import models
from django.urls import reverse


class SlideDeck (models.Model):
    title = models.CharField (max_length=100)
    text = models.TextField ()
   
    def __str__(self):
        return self.title
