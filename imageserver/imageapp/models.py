from django.db import models

# Create your models here.
class Image(models.Model):
    imagename = models.CharField(max_length=100)
    imagehashcode = models.CharField(max_length=100)

    def __str__(self):
        return self.imagehashcode

    def filename(self):
        return self.imagename