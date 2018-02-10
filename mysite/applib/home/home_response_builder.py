from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype
from applib.author_website_keys import AuthorWebsiteKeys as awk

class HomeResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_mature_index_css(self):
        home_index_css_path = self.get_page_path(
            app=awk.HOME, filetype=awk.CSS, page="home_index"
        )
        home_index_css = self.get_file_contents(home_index_css_path)

        return home_index_css

    def get_mature_index_html(self):
        home_index_html_path = self.get_page_path(
            app=awk.HOME, page="home_index"
        )
        home_index_html = self.get_file_contents(home_index_html_path)

        return home_index_html

    def get_index_response(self):
        title = "The Blood of the World"

        global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
        header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
        footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
        archetype_css_path = self.get_page_path(
            app=awk.HOME, filetype=awk.CSS, page="warden"
        )
        mature_home_index_css = self.get_mature_index_css()

        all_css_L = self.get_file_contents_for_list(
            file_list=[global_css_path,header_css_path,footer_css_path,
                       archetype_css_path]
        )
        all_css_L.append(mature_home_index_css)

        mature_home_index_html = self.get_mature_index_html()
        all_body_html_L = [mature_home_index_html]

        implemented_html = self.stitch_and_get_page(
            title=title, all_css_L=all_css_L, all_body_html_L=all_body_html_L
        )

        return HttpResponse(implemented_html)
