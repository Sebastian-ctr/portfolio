from django.contrib import admin

# Register your models here.
from .models import Photo, PhotoImage, Home_photo

class PhotoImageAdmin(admin.StackedInline):
    model = PhotoImage


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoImageAdmin]

    class Meta:
        model = Photo


@admin.register(PhotoImage)
class PhotoImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Home_photo)