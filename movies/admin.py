from django.contrib import admin

from .models import Movie, Genre

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
