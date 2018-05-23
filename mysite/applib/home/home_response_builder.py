from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype
from applib.author_website_keys import AuthorWebsiteKeys as awk

class HomeResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_index_response(self):
        title = "The Blood of the World - by Jeremy Bruce Adams"
        description = 'The Blood of the World is an upcoming fantasy series by aspiring author Jeremy Bruce Adams. '\
                      + '''The first novel, A Warden's Calling, tells the story of Araja, a slave cursed with '''\
                      + '''the inability to wield magic, yet destined to change the world.'''

        #get paths to all css files
        #global, website header, website footer
        global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
        header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
        footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
        #archetype css
        archetype_css_path = self.get_page_path(
            app=awk.HOME, filetype=awk.CSS,
            dependence=awk.PLATFORM_INDEPENDENT, page="warden"
        )
        #platform independent and dependent css for the home page
        home_index_independent_css_path = self.get_page_path(
            app=awk.HOME, filetype=awk.CSS,
            dependence=awk.PLATFORM_INDEPENDENT, page="home_index"
        )
        home_index_dependent_css_path = self.get_page_path(
            app=awk.HOME, filetype=awk.CSS, page="home_index"
        )
        #get string representing all css from all file sources
        all_css_L = self.get_file_contents_for_list(
            file_list=[
                global_css_path,
                header_css_path,
                footer_css_path,
                archetype_css_path,
                home_index_independent_css_path,
                home_index_dependent_css_path
            ]
        )

        #get paths to all body html files
        home_index_independent_html_path = self.get_page_path(
            app=awk.HOME, page="home_index",
            dependence=awk.PLATFORM_INDEPENDENT
        )
        #get string representing all body html from all file sources
        all_body_html_L = self.get_file_contents_for_list(
            file_list=[
                home_index_independent_html_path
            ]
        )

        #get paths to all js function files
        global_js_path = self.get_page_path(filetype=awk.JS, path_or_url=awk.STATICURL,
                                            dependence=awk.PLATFORM_INDEPENDENT, page="global_functions")
        home_index_js_path = self.get_page_path(app=awk.HOME, filetype=awk.JS, path_or_url=awk.STATICURL,
                                           dependence=awk.PLATFORM_INDEPENDENT, page="home_index_functions")
        all_js_L = [global_js_path, home_index_js_path]

        #stitch final response from all css string, all html string,
        #and all js paths
        implemented_html = self.stitch_and_get_page(
            title=title, description=description, all_css_L=all_css_L, all_body_html_L=all_body_html_L,
            all_js_L=all_js_L
        )

        return HttpResponse(implemented_html)
