from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype

class HomeResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self)
        self.home_css_dir = self.get_home_css_dir()

    def get_home_css_dir(self):
        static_url = get_static_url()
        css_dir = static_url+"/frontend/apps/home/css"
        return css_dir

    def get_home_css_file(self,archetype_index):
        cssfiles_L = [
            "warden.css",
            "rebel.css",
            "champion.css",
            "architect.css",
            "conqueror.css",
            "exile.css"
        ]
        return self.home_css_dir+"/"+cssfiles_L[archetype_index]

    def get_index_response(self):
        css = self.get_home_css_file(self.archetype.WARDEN)
        skeleton = self.get_raw_skeleton_html(self.client_tracker.PC)
        header = self.get_raw_header_html(self.client_tracker.PC)
        footer = self.get_raw_footer_html(self.client_tracker.PC)

        body_test_angular = """<div>
        Write some text in this text booox:
        <input type="text" ng-model="sometext" />
        <h1>Hello {{sometext}}</h1>
</div>
"""
        final_html = skeleton
        implementation_L = [
            ["AWVAR_CSS",css],
            ["AWVAR_ANGULARJS",self.get_staticurl_angular_js_min()],
            ["AWVAR_HTML_HEADER",header],
            ["AWVAR_HTML_BODY",body_test_angular],
            ["AWVAR_HTML_FOOTER",footer]
        ]
        for imp in implementation_L:
            final_html = self.implement_html(final_html,imp[0],imp[1])

        return HttpResponse(final_html)
