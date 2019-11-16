from django.db import models


class Contact (models.Model):
    name = models.CharField (max_length=100)
    email = models.EmailField ()
 
    def __str__(self):
        return "%s [%s]" % (self.name, self.email)
