import os
import re
from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype
from applib.author_website_keys import AuthorWebsiteKeys as awk

class NewsResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_index_response(self):
        #coming_soon_html = self.get_coming_soon_html()

        title = "The Blood of the World - News"
        description = "no description"

        #get paths to all css files
        global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
        header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
        footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
        # archetype css
        archetype_css_path = self.get_page_path(
            app=awk.NEWS, filetype=awk.CSS,
            dependence=awk.PLATFORM_INDEPENDENT, page="warden"
        )
        # platform-independent and dependent css for the news index page
        news_index_independent_css_path = self.get_page_path(
            app=awk.NEWS, filetype=awk.CSS,
            dependence=awk.PLATFORM_INDEPENDENT, page="news_index"
        )
        news_index_dependent_css_path = self.get_page_path(
            app=awk.NEWS, filetype=awk.CSS,
            page="news_index"
        )

        #get string representing all css from all file sources
        all_css_L = self.get_file_contents_for_list(
            file_list=[
                global_css_path,
                header_css_path,
                footer_css_path,
                archetype_css_path,
                news_index_independent_css_path,
                news_index_dependent_css_path
            ]
        )

        #get paths to all html body files
        news_index_independent_html_path = self.get_page_path(
            app=awk.NEWS, page="news_index",
            dependence=awk.PLATFORM_INDEPENDENT
        )
        #get string representing all body html from all file sources
        all_body_html_L = self.get_file_contents_for_list(
            file_list=[
                news_index_independent_html_path
            ]
        )

        #get paths to all js function files
        news_index_independent_js_path = self.get_page_path(
            app=awk.NEWS, filetype=awk.JS, page="news_index_functions",
            dependence=awk.PLATFORM_INDEPENDENT, path_or_url=awk.STATICURL
        )
        calendar_js_path = self.get_page_path(
            app=awk.NEWS, filetype=awk.JS, page="calendar_functions",
            dependence=awk.PLATFORM_INDEPENDENT, path_or_url=awk.STATICURL
        )

        all_js_L = [
            news_index_independent_js_path,
            calendar_js_path
        ]

        #stitch final response from all css string, html string,
        #and js paths
        implemented_html = self.stitch_and_get_page(
            title=title, description=description, all_css_L=all_css_L,
            all_body_html_L=all_body_html_L, all_js_L=all_js_L
        )

        return HttpResponse(implemented_html)
