from applib.archetype import Archetype
from applib.client_tracker import ClientTracker
from applib.website_methods import *
from applib.author_website_keys import AuthorWebsiteKeys as awk

class ResponseBuilder:
    def __init__(self,request):
        self.request = request
        self.archetype = Archetype()
        self.client_tracker = ClientTracker(self.request)

    def get_directory(
        self, app=awk.GLOBAL, filetype=awk.HTML, path_or_url=awk.STATICROOT,
        frontend_or_content=awk.FRONTEND
    ):
        """
        gets string representing filesystem path (STATICROOT) or url (STATICURL)
        to an app-specific, filetype-specific directory of static files

        Args:
            app (int): from AuthorWebsiteKeys, indicates the django app where
                frontend content will be drawn from
            filetype (int): from AuthorWebsiteKeys, indicates the filetype
                (HTML,CSS,JS) directory where frontend content will be drawn
                from
            path_or_url (int): from AuthorWebsiteKeys, indicates whether the
                returned path will be a filesystem path or a static url

        Returns:
            (string): filesystem or static url path to frontend content
                directory
        """

        path = None

        if path_or_url == awk.STATICROOT:
            path = get_static_root()
        elif path_or_url == awk.STATICURL:
            path = get_static_url()

        if frontend_or_content == awk.FRONTEND:
            path += "/frontend"

            if app == awk.GLOBAL:
                path += "/global"
            else:
                path += "/apps"

        if app == awk.HOME:
            path += "/home"
        elif app == awk.ARTICLES:
            path += "/articles"

        if frontend_or_content == awk.FRONTEND:
            if filetype == awk.HTML:
                path += "/html"
            elif filetype == awk.CSS:
                path += "/css"
            elif filetype == awk.JS:
                path += "/js"

        if frontend_or_content == awk.CONTENT:
            if filetype == awk.JPG:
                path += "/img"

        return path

    def get_page_path(
        self, app=awk.GLOBAL, filetype=awk.HTML, path_or_url=awk.STATICROOT,
        frontend_or_content=awk.FRONTEND, page="ws_skeleton"
    ):
        """
        get path to a frontend content page, whether as on the filesystem
        (STATICROOT) or as it would appear on an html page (STATICURL)

        Args:
            app (int): from AuthorWebsiteKeys, indicates the django app where
                frontend content will be drawn from
            filetype (int): from AuthorWebsiteKeys, indicates the filetype
                (HTML,CSS,JS) directory where frontend content will be drawn
                from
            path_or_url (int): from AuthorWebsiteKeys, indicates whether the
                returned path will be a filesystem path or a static url

        Returns:
            (string): full path to a frontend html, css, or js page
        """

        directory = self.get_directory(app, filetype, path_or_url,
            frontend_or_content)
        device_string = ""

        if frontend_or_content == awk.FRONTEND:
            if self.client_tracker.device_D['pc']:
                device_string = ".pc"
            elif self.client_tracker.device_D['mobile']:
                device_string = ".mobile"
            elif self.client_tracker.device_D['tablet']:
                device_string = ".tablet"
            else:
                device_string = ".pc"

        suffix = ""
        if filetype == awk.HTML:
            suffix = ".html"
        elif filetype == awk.CSS:
            suffix = ".css"
        elif filetype == awk.JS:
            suffix = ".js"
        elif filetype == awk.JPG:
            suffix = ".jpg"

        full_path = directory + "/" + page + device_string + suffix

        return full_path

    def get_file_contents(self, path=None):
        """
        get string representing HTML, CSS, or JS contents of a file

        Args:
            path (string): full path to desired file

        Returns:
            (string): contents of HTML, CSS, or JS file
        """

        return open(path,"r").read()

    def get_file_contents_for_list(self, file_list=None):
        return [self.get_file_contents(f) for f in file_list]

    def concatenate_file_content_strings(self, strings_list=None):
        return "".join(strings_list)

    def stitch_and_get_page(
        self, title=None, all_css_L=None, all_body_html_L=None
    ):
        skeleton_path = self.get_page_path()
        skeleton_html = self.get_file_contents(skeleton_path)
        header_path = self.get_page_path(page="ws_header")
        header_html = self.get_file_contents(header_path)
        footer_path = self.get_page_path(page="ws_footer")
        footer_html = self.get_file_contents(footer_path)

        all_css_string = self.concatenate_file_content_strings(all_css_L)
        all_html_body_string = \
            self.concatenate_file_content_strings(all_body_html_L)

        implemented_html = skeleton_html\
            .replace("AWVAR_TITLE",title)\
            .replace("AWVAR_CSS",all_css_string)\
            .replace("AWVAR_HTML_HEADER",header_html)\
            .replace("AWVAR_HTML_BODY",all_html_body_string)\
            .replace("AWVAR_HTML_FOOTER",footer_html)\

        return implemented_html


    #def get_staticurl_global_frontend_dir(self):
    #    static_url = get_static_url()
    #    global_dir = static_url+"/frontend/global"
    #    return global_dir
    #def get_staticurl_global_css_dir(self):
    #    return self.get_staticurl_global_frontend_dir()+"/css"
    #def get_staticurl_global_html_dir(self):
    #    return self.get_staticurl_global_frontend_dir()+"/html"
    #def get_staticurl_global_js_dir(self):
    #    return self.get_staticurl_global_frontend_dir()+"/js"
    #def get_staticurl_angular_js_dev(self):
    #    return self.get_staticurl_global_js_dir()+"/angular.js"
    #def get_staticurl_angular_js_min(self):
    #    return self.get_staticurl_global_js_dir()+"/angular.min.js"

    #def get_staticroot_global_frontend_dir(self):
    #    static_root = get_static_root()
    #    global_dir = static_root+"/frontend/global"
    #    return global_dir
    #def get_staticroot_global_css_dir(self):
    #    return self.get_staticroot_global_frontend_dir()+"/css"
    #def get_staticroot_global_html_dir(self):
    #    return self.get_staticroot_global_frontend_dir()+"/html"
    #def get_staticroot_global_js_dir(self):
    #    return self.get_staticroot_global_frontend_dir()+"/js"
    #def get_staticroot_angular_js_dev(self):
    #    return self.get_staticroot_global_js_dir()+"/angular.js"
    #def get_staticroot_angular_js_min(self):
    #    return self.get_staticroot_global_js_dir()+"/angular.min.js"

    #def get_staticroot_global_css(self,device):
    #    path = self.get_staticroot_global_css_dir()
    #    if device == self.client_tracker.MOBILE:
    #        path += "/global.mobile.css"
    #    else:
    #        path += "/global.css"
    #    raw_css = open(path,"r").read()
    #    return raw_css

    #def get_staticroot_wsheader_css(self,device):
    #    path = self.get_staticroot_global_css_dir()
    #    if device == self.client_tracker.MOBILE:
    #        path += "/ws_header.mobile.css"
    #    else:
    #        path += "/ws_header.css"
    #    raw_css = open(path,"r").read()
    #    return raw_css

    #def get_staticroot_wsfooter_css(self,device):
    #    path = self.get_staticroot_global_css_dir()
    #    if device == self.client_tracker.MOBILE:
    #        path += "/ws_footer.mobile.css"
    #    else:
    #        path += "/ws_footer.css"
    #    raw_css = open(path,"r").read()
    #    return raw_css

    #def get_raw_skeleton_html(self,device):
    #    path = self.get_staticroot_global_html_dir()
    #    if device == self.client_tracker.MOBILE:
    #        path += "/ws_skeleton.mobile.html"
    #    else:
    #        path += "/ws_skeleton.html"
    #    raw_html = open(path,"r").read()
    #    return raw_html

    #def get_raw_header_html(self,device):
    #    path = self.get_staticroot_global_html_dir()
    #    if device == self.client_tracker.MOBILE:
    #        path += "/ws_header.mobile.html"
    #    else:
    #        path += "/ws_header.html"
    #    raw_html = open(path,"r").read()
    #    return raw_html

    #def get_raw_footer_html(self,device):
    #    path = self.get_staticroot_global_html_dir()
    #    if device == self.client_tracker.MOBILE:
    #        path += "/ws_footer.mobile.html"
    #    else:
    #        path += "/ws_footer.html"
    #    raw_html = open(path,"r").read()
    #    return raw_html

    #def implement_html(self,raw_html,html_key,html_value):
    #    implemented_html = raw_html.replace(
    #        html_key,html_value
    #    )
    #    return implemented_html
