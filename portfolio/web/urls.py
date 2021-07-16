from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('press/', views.press, name='press'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('photos/<int:id>/', views.photos_detail, name='album_details'), 
    path('films/',views.films, name='films'), 
    path('films/<int:id>/', views.films_detail, name='films_detail'),    
]