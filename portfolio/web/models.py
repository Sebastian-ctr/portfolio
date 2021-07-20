from django.db import models

# Create your models here.
class Home_photo(models.Model):
    tittle = models.CharField(max_length=50)
    image = models.FileField(upload_to='media_cdn')

    def __str__(self):
        return self.tittle


class About(models.Model):
    content = models.TextField(default=None)
    image = models.FileField(upload_to='media_cdn', default=None)

    def __str__(self):
        return self.tittle
    


class Photo(models.Model):
    tittle = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.tittle

class PhotoImage(models.Model):
    photo = models.ForeignKey(Photo, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='media_cdn')


class Film(models.Model):
    url = models.CharField(max_length=200)
    tittle = models.TextField()

    def __str__(self):
        return self.tittle


class Music(models.Model):
    url = models.CharField(max_length=200)
    tittle = models.TextField()

    def __str__(self):
        return self.tittle

class Text(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.tittle

class Publication(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.tittle

    
    
