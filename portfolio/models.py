from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self): # this will view the title when viewing in admin window
        return self.title