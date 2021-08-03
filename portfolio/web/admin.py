from django.contrib import admin

# Register your models here.
from .models import Photo, PhotoImage, Home_photo, Film, Music, About, Text, Publication, Contact

class PhotoImageAdmin(admin.StackedInline):
    model = PhotoImage


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoImageAdmin]

    class Meta:
        model = Photo


@admin.register(PhotoImage)
class PhotoImageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):

        return{}


class TextAdmin(admin.ModelAdmin):
    list_display = ["tittle", "data"]

    


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ["tittle", "data"]

    

admin.site.register(Home_photo)
admin.site.register(Film)
admin.site.register(Music)
admin.site.register(About)
admin.site.register(Text, TextAdmin)
admin.site.register(Publication, PublicationsAdmin)
admin.site.register(Contact)
