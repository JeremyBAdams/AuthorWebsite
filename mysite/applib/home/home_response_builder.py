from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype

class HomeResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_staticroot_home_archetype_css_dir(self):
        static_root = get_static_root()
        css_dir = static_root+"/frontend/apps/home/css"
        return css_dir

    def get_staticroot_home_archetype_css(self,archetype_index):
        cssfiles_L = [
            "warden.css",
            "rebel.css",
            "champion.css",
            "architect.css",
            "conqueror.css",
            "exile.css"
        ]
        cssfile = self.get_staticroot_home_archetype_css_dir()+"/" \
                  + cssfiles_L[archetype_index]
        raw_css = open(cssfile,"r").read()
        return raw_css

    def get_index_response(self):
        skeleton_html = self.get_raw_skeleton_html(self.client_tracker.PC)
        header_html = self.get_raw_header_html(self.client_tracker.PC)
        footer_html = self.get_raw_footer_html(self.client_tracker.PC)

        global_css = self.get_staticroot_global_css(self.client_tracker.PC)
        header_css = self.get_staticroot_wsheader_css(self.client_tracker.PC)
        footer_css = self.get_staticroot_wsfooter_css(self.client_tracker.PC)

        archetype_int = get_random_archetype_integer()
        archetype_css = self.get_staticroot_home_archetype_css(
            archetype_int
        )
        all_css = "\n".join([
            global_css,header_css,footer_css,archetype_css
        ])+"\n"

        body_test_angular = ""
        final_html = skeleton_html
        implementation_L = [
            ["AWVAR_TITLE","The Blood of the World"],
            ["AWVAR_CSS",all_css],
            ["AWVAR_ANGULARJS",self.get_staticurl_angular_js_min()],
            ["AWVAR_HTML_HEADER",header_html],
            ["AWVAR_HTML_BODY",body_test_angular],
            ["AWVAR_HTML_FOOTER",footer_html]
        ]
        for imp in implementation_L:
            final_html = self.implement_html(final_html,imp[0],imp[1])

        return HttpResponse(final_html)
