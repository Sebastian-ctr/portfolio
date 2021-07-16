from django.shortcuts import render, get_object_or_404
from .models import Photo, PhotoImage, Home_photo

# Create your views here.
def home(request):
    photo = Home_photo.objects.all()
    context = {
        'photo':photo,
    }
    return render(request, 'home.html')


def photos(request):
    album = Photo.objects.all()
    context = {
        'album': album,
    }
    return render(request, 'photos.html', context)

def press(request):
    return render(request, 'press.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def photos_detail(request, id):
    photo = get_object_or_404(Photo, id=id)
    photos = PhotoImage.objects.filter(photo=photo)
    context = {
        'photo':photo,
        'photos':photos
    }
    return render(request,'photos_detail.html', context)

def films(request):
    return render(request, 'films.html')