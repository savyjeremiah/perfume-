from django.db import models

from django.db import models
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

class Perfume(models.Model):
    name = models.CharField(max_length=200)
    sizes = models.CharField(max_length=100)
    grp = models.CharField(max_length=100)
    image = models.ImageField(upload_to='perfume_images/')
    prices = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

   
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.resize((300, 300)) 
            thumb_io = io.BytesIO()
            img.save(thumb_io, img.format)
            thumb_io.seek(0)
            self.image = InMemoryUploadedFile(thumb_io, None, self.image.name, 'image/jpeg', thumb_io.getbuffer().nbytes, None)
        super().save(*args, **kwargs)


class SearchEngine(models.Model):
    search_term = models.CharField(max_length=200)
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.search_term
