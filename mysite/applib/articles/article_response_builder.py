from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype

class ArticleResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self)
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

    def get_index_response(self):
        cssfile = self.get_archetype_css_file(self.archetype.WARDEN)
        html_header = self.get_header_html_string()
        html_footer = self.get_footer_html_string()

        response_string = """<!DOCTYPE HTML>
    <head>
    <link rel="stylesheet" type ="text/css" href="%s">
    </head>
    <body>
        <div class="my_div">
        %s
        Index page for articles app<br>
        Welcome Friendo<br><br>
        %s
        </div>
    </body>
    """ % (cssfile ,html_header , html_footer)

        return HttpResponse(response_string)

    def get_article_response(self,archetype_index):
        pass
