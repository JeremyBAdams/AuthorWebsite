from django.contrib import admin
from .models import Pseudonym, Series, Palette, Article

# Register your models here.
admin.site.register(Pseudonym)
admin.site.register(Series)
admin.site.register(Palette)
admin.site.register(Article)
