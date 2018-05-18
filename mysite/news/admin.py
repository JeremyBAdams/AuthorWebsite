from django.contrib import admin
from .models import NewsArticle, Event

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(Event)
