from django.db import models

# Create your models here.
class Home_photo(models.Model):
    tittle = models.CharField(max_length=50)
    image = models.FileField(upload_to='media_cdn')

    def __str__(self):
        return self.tittle


class About(models.Model):
    pass


class Photo(models.Model):
    tittle = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.tittle

class PhotoImage(models.Model):
    photo = models.ForeignKey(Photo, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='media_cdn')

    
    
