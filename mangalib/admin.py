from django.contrib import admin
from .models import models, Auteur,livre

# Register your models here.
admin.site.register(Auteur)
admin.site.register(livre)

