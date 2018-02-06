import os
import re
from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype

class ArticleResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_staticroot_article_html_dir(self):
        static_root = get_static_root()
        html_dir = static_root+"/frontend/apps/articles/html"
        return html_dir

    def get_staticroot_article_index_html(self):
        path = self.get_staticroot_article_html_dir()+"/article_index.html"
        html = open(path,"r").read()
        return html

    def get_staticroot_article_response_html(self):
        path = self.get_staticroot_article_html_dir()+"/article_response.html"
        html = open(path,"r").read()
        return html

    def get_staticroot_article_css_dir(self):
        static_root = get_static_root()
        css_dir = static_root+"/frontend/apps/articles/css"
        return css_dir

    def get_staticroot_article_general_css(self,device):
        cssfile = self.get_staticroot_article_css_dir()+"/general.css"
        raw_css = open(cssfile,"r").read()
        return raw_css

    def get_staticroot_article_index_css(self,device):
        cssfile = self.get_staticroot_article_css_dir()+"/index.css"
        raw_css = open(cssfile,"r").read()
        return raw_css

    def get_staticroot_article_archetype_css(self,archetype_index):
        cssfiles_L = [
            "warden.css",
            "rebel.css",
            "champion.css",
            "architect.css",
            "conqueror.css",
            "exile.css"
        ]
        cssfile = self.get_staticroot_article_css_dir()+"/" \
                  + cssfiles_L[archetype_index]
        raw_css = open(cssfile,"r").read()
        return raw_css

    def get_index_response(self):
        skeleton_html = self.get_raw_skeleton_html(self.client_tracker.PC)
        header_html = self.get_raw_header_html(self.client_tracker.PC)
        footer_html = self.get_raw_footer_html(self.client_tracker.PC)
        index_html = self.get_staticroot_article_index_html()

        global_css = self.get_staticroot_global_css(self.client_tracker.PC)
        header_css = self.get_staticroot_wsheader_css(self.client_tracker.PC)
        footer_css = self.get_staticroot_wsfooter_css(self.client_tracker.PC)
        index_css = self.get_staticroot_article_index_css(self.client_tracker.PC)

        archetype_int = self.archetype.WARDEN
        archetype_css = self.get_staticroot_article_archetype_css(
            archetype_int
        )
        all_css = "\n".join([
            global_css,header_css,footer_css,archetype_css, index_css
        ])

        final_html = skeleton_html

        article_index_body = self.get_staticroot_article_index_html()

        implementation_L = [
            ["AWVAR_TITLE","The Blood of the World"],
            ["AWVAR_CSS",all_css],
            ["AWVAR_ANGULARJS",self.get_staticurl_angular_js_min()],
            ["AWVAR_HTML_HEADER",header_html],
            ["AWVAR_HTML_BODY",article_index_body],
            ["AWVAR_HTML_FOOTER",footer_html]
        ]
        for imp in implementation_L:
            final_html = self.implement_html(final_html,imp[0],imp[1])

        return HttpResponse(final_html)

    def get_article_response(self):
        skeleton_html = self.get_raw_skeleton_html(self.client_tracker.PC)
        header_html = self.get_raw_header_html(self.client_tracker.PC)
        footer_html = self.get_raw_footer_html(self.client_tracker.PC)

        global_css = self.get_staticroot_global_css(self.client_tracker.PC)
        article_css = self.get_staticroot_article_general_css(self.client_tracker.PC)
        header_css = self.get_staticroot_wsheader_css(self.client_tracker.PC)
        footer_css = self.get_staticroot_wsfooter_css(self.client_tracker.PC)

        archetype_int = self.archetype.WARDEN
        archetype_css = self.get_staticroot_article_archetype_css(
            archetype_int
        )

        final_html = skeleton_html
        #check if the requested path exists
        article_html_path = get_static_root() \
                            + self.request.path \
                            + ".html"

        article_var_bg_image = get_static_url() \
                               + "/articles/img/" \
                               + self.request.path.split("/")[-1] \
                               + ".jpg"

        if os.path.exists(article_html_path):
            article_html = open(article_html_path,"r").read().rstrip()
            article_html_body = re.compile("<body>(.+?)</body>",re.DOTALL).\
                search(article_html).group(1)

            article_template = self.get_staticroot_article_response_html()

            mature_article_html = article_template.replace(
                "ARTICLE_VAR_CONTENT",
                article_html_body
            )

            mature_article_css = "\n".join([
                global_css,
                article_css.replace(
                    "ARTICLE_VAR_BG_IMAGE",
                    article_var_bg_image
                ),
                header_css,
                footer_css,
                archetype_css
            ])

            implementation_L = [
                ["AWVAR_TITLE","The Blood of the World"],
                ["AWVAR_CSS",mature_article_css],
                ["AWVAR_ANGULARJS",self.get_staticurl_angular_js_min()],
                ["AWVAR_HTML_HEADER",header_html],
                ["AWVAR_HTML_BODY",mature_article_html],
                ["AWVAR_HTML_FOOTER",footer_html]
            ]
            for imp in implementation_L:
                final_html = self.implement_html(final_html,imp[0],imp[1])
        else:
            final_html = "Sorry, that article could not be found."

        return HttpResponse(final_html)
