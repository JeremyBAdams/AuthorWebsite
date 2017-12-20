from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

class ArticleManager:

    def __init__(self):
        self.WARDEN=0
        self.REBEL=1
        self.CHAMPION=2
        self.ARCHITECT=3
        self.CONQUEROR=4
        self.EXILE=5

        self.article_css_dir = self.get_article_css_dir()

    def get_article_css_dir(self):
        static_url = settings.STATIC_URL
        css_dir = static_url+"/frontend/apps/articles/css"
        return css_dir

    def get_archetype_css_file(self,archetype):
        cssfiles_L = [
            "warden.css",
            "rebel.css",
            "champion.css",
            "architect.css",
            "conqueror.css",
            "exile.css"
        ]
        return self.article_css_dir+"/"+cssfiles_L[archetype]
