from django.db import models
from django.utils import timezone
# from datetime import date

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    url = models.URLField(blank=True)
    # date = models.DateField(default=timezone.now())
    def __str__(self): # this will view the title when viewing in admin window
        return self.title