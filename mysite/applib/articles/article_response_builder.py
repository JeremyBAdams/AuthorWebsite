from applib.website_methods import *
from applib.response_builder import ResponseBuilder

class ArticleResponseBuilder(ResponseBuilder):

    def __init__(self):
        self.article_css_dir = self.get_article_css_dir()

    def get_article_css_dir(self):
        static_url = get_static_url()
        css_dir = static_url+"/frontend/apps/articles/css"
        return css_dir

    def get_archetype_css_file(self,archetype_index):
        cssfiles_L = [
            "warden.css",
            "rebel.css",
            "champion.css",
            "architect.css",
            "conqueror.css",
            "exile.css"
        ]
        return self.article_css_dir+"/"+cssfiles_L[archetype_index]
