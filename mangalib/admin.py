from django.contrib import admin
from .models import models, Auteur,livre


# Register your models here.
@admin.register(Auteur) # ou admin.site.register(Auteur,AuteurAdmin) mais il est mis en bas sur <1>
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(livre) # ou admin.site.register(livre,LivreAdmin) mais il est mis en bas sur <1>
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur','quantity')
    list_filter = ['auteur']
    search_fields = ['titre']



#mais il est mis ici sur <1>
