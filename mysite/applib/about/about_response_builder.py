import os
import re
from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype
from applib.author_website_keys import AuthorWebsiteKeys as awk

class AboutResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_index_response(self):
        #coming_soon_html = self.get_coming_soon_html()

        title = "About the Author - Jeremy Bruce Adams"
        description = "no description"

        #get paths to all css files
        global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
        header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
        footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
        #archetype css
        archetype_css_path = self.get_page_path(
            app=awk.ABOUT, filetype=awk.CSS,
            dependence=awk.PLATFORM_INDEPENDENT, page="warden"
        )
        #platform-independent and dependent css for the about page
        about_index_independent_css_path = self.get_page_path(
            app=awk.ABOUT, filetype=awk.CSS,
            dependence=awk.PLATFORM_INDEPENDENT, page="about_index"
        )
        about_index_dependent_css_path = self.get_page_path(
            app=awk.ABOUT, filetype=awk.CSS,
            page="about_index"
        )

        #get string representing all css from all file sources
        all_css_L = self.get_file_contents_for_list(
            file_list=[
                global_css_path,
                header_css_path,
                footer_css_path,
                archetype_css_path,
                about_index_independent_css_path,
                about_index_dependent_css_path
            ]
        )

        #get paths to all body html files
        about_index_independent_html_path = self.get_page_path(
            app=awk.ABOUT, page="about_index",
            dependence=awk.PLATFORM_INDEPENDENT
        )
        #get string representing all body html from all file sources
        all_body_html_L = self.get_file_contents_for_list(
            file_list=[
                about_index_independent_html_path
            ]
        )

        #get paths to all js function files
        all_js_L = []

        #stitch final response from all css string, html string,
        #and js paths
        implemented_html = self.stitch_and_get_page(
            title=title, description=description, all_css_L=all_css_L, all_body_html_L=all_body_html_L,
            all_js_L=all_js_L
        )

        return HttpResponse(implemented_html)
