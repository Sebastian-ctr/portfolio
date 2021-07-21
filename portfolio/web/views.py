from django.shortcuts import render, get_object_or_404
from .models import Photo, PhotoImage, Home_photo, Film, Music, About

# Create your views here.
def home(request):
    photo = Home_photo.objects.all()
    context = {
        'photo':photo,
    }
    return render(request, 'home.html', context)


def photos(request):
    album = Photo.objects.all()
    context = {
        'album': album,
    }
    return render(request, 'photos.html', context)

def press(request):
    return render(request, 'press.html')

def about(request):
    about = About.objects.first()
    context = {
        'about':about
    }
    return render(request, 'about.html', context)


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
    films = Film.objects.all()
    context = {
        'films':  films,
    }
    return render(request, 'films.html', context)

def films_detail(request, id):
    film = get_object_or_404(Film, id=id)
    context = {
        'film':film
    }
    return render(request, 'films_detail.html', context)


def music(request):
    music = Music.objects.all()
    context = {
        'music': music
    }
    return render(request, 'music.html', context)

def music_detail(request, id):
    music = get_object_or_404(Music, id=id)
    context = {
        'music':music
    }
    return render(request, 'music_detail.html', context)