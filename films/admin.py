from django.contrib import admin

from films.models import Film

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'director', 'rating', 'genre', 'runtime', 'description', 'photo']
    search_fields = ['title', 'year', 'director', 'rating', 'genre', 'runtime', 'description', 'photo']
    list_filter = ['title']

admin.site.register(Film, UserAdmin)


