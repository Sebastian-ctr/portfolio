from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def films(request):
    return render(request, 'film.html')

def press(request):
    return render(request, 'press.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')