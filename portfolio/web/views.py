from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Photo, PhotoImage, Home_photo, Film, Music, About, Text, Publication

# Create your views here.
def home(request):
    photo = Home_photo.objects.all()
    context = {
        'photo':photo,
    }
    return render(request, 'home.html', context)


def photos(request):
    album = Photo.objects.all().order_by("-id")
    paginator = Paginator(album, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'album': album,
        'page_obj':page_obj,
    }
    return render(request, 'photos.html', context)

#press is text
def press(request):
    text = Text.objects.all().order_by("-data")
    paginator = Paginator(text, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'text': text,
        'page_obj':page_obj,
    }
    return render(request, 'press.html', context)




def press_detail(request, id):
    text = get_object_or_404(Text, id=id)
    context = {
        'text':text,
    }
    return render(request, 'press_detail.html', context)

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
    films = Film.objects.all().order_by("-id")
    paginator = Paginator(films, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'films':  films,
        'page_obj':page_obj,
    }
    return render(request, 'films.html', context)

def films_detail(request, id):
    film = get_object_or_404(Film, id=id)
    context = {
        'film':film
    }
    return render(request, 'films_detail.html', context)


def music(request):
    music = Music.objects.all().order_by("-id")
    paginator = Paginator(music, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'music': music,
        'page_obj':page_obj,
    }
    return render(request, 'music.html', context)

def music_detail(request, id):
    music = get_object_or_404(Music, id=id)
    context = {
        'music':music
    }
    return render(request, 'music_detail.html', context)


def publications(request):
    publication = Publication.objects.all()
    paginator = Paginator(publication, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'publication': publication,
        'page_obj': page_obj,
    }
    return render(request, 'publications.html', context)

def publications_detail(request, id):
    pass