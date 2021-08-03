from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('text/', views.press, name='press'),
    path('text/<int:id>/', views.press_detail, name='press_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('photos/<int:id>/', views.photos_detail, name='album_details'), 
    path('films/',views.films, name='films'), 
    path('films/<int:id>/', views.films_detail, name='films_detail'),
    path('music/', views.music, name='music'), 
    path('music/<int:id>/', views.music_detail, name='music_detail'),
    path('publications/', views.publications, name='publications'),
    path('publications/<int:id>/', views.publications_detail, name='publications_detail'),   
]