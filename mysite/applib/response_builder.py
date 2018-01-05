from applib.archetype import Archetype
from applib.client_tracker import ClientTracker
from applib.website_methods import *

class ResponseBuilder:
    def __init__(self,request):
        self.request = request
        self.archetype = Archetype()
        self.client_tracker = ClientTracker()

    def get_staticurl_global_frontend_dir(self):
        static_url = get_static_url()
        global_dir = static_url+"/frontend/global"
        return global_dir
    def get_staticurl_global_css_dir(self):
        return self.get_staticurl_global_frontend_dir()+"/css"
    def get_staticurl_global_html_dir(self):
        return self.get_staticurl_global_frontend_dir()+"/html"
    def get_staticurl_global_js_dir(self):
        return self.get_staticurl_global_frontend_dir()+"/js"
    def get_staticurl_angular_js_dev(self):
        return self.get_staticurl_global_js_dir()+"/angular.js"
    def get_staticurl_angular_js_min(self):
        return self.get_staticurl_global_js_dir()+"/angular.min.js"

    def get_staticroot_global_frontend_dir(self):
        static_root = get_static_root()
        global_dir = static_root+"/frontend/global"
        return global_dir
    def get_staticroot_global_css_dir(self):
        return self.get_staticroot_global_frontend_dir()+"/css"
    def get_staticroot_global_html_dir(self):
        return self.get_staticroot_global_frontend_dir()+"/html"
    def get_staticroot_global_js_dir(self):
        return self.get_staticroot_global_frontend_dir()+"/js"
    def get_staticroot_angular_js_dev(self):
        return self.get_staticroot_global_js_dir()+"/angular.js"
    def get_staticroot_angular_js_min(self):
        return self.get_staticroot_global_js_dir()+"/angular.min.js"

    def get_staticroot_global_css(self,device):
        path = self.get_staticroot_global_css_dir()
        if device == self.client_tracker.MOBILE:
            path += "/global.mobile.css"
        else:
            path += "/global.css"
        raw_css = open(path,"r").read()
        return raw_css

    def get_staticroot_wsheader_css(self,device):
        path = self.get_staticroot_global_css_dir()
        if device == self.client_tracker.MOBILE:
            path += "/ws_header.mobile.css"
        else:
            path += "/ws_header.css"
        raw_css = open(path,"r").read()
        return raw_css

    def get_staticroot_wsfooter_css(self,device):
        path = self.get_staticroot_global_css_dir()
        if device == self.client_tracker.MOBILE:
            path += "/ws_footer.mobile.css"
        else:
            path += "/ws_footer.css"
        raw_css = open(path,"r").read()
        return raw_css

    def get_raw_skeleton_html(self,device):
        path = self.get_staticroot_global_html_dir()
        if device == self.client_tracker.MOBILE:
            path += "/ws_skeleton.mobile.html"
        else:
            path += "/ws_skeleton.html"
        raw_html = open(path,"r").read()
        return raw_html

    def get_raw_header_html(self,device):
        path = self.get_staticroot_global_html_dir()
        if device == self.client_tracker.MOBILE:
            path += "/ws_header.mobile.html"
        else:
            path += "/ws_header.html"
        raw_html = open(path,"r").read()
        return raw_html

    def get_raw_footer_html(self,device):
        path = self.get_staticroot_global_html_dir()
        if device == self.client_tracker.MOBILE:
            path += "/ws_footer.mobile.html"
        else:
            path += "/ws_footer.html"
        raw_html = open(path,"r").read()
        return raw_html

    def implement_html(self,raw_html,html_key,html_value):
        implemented_html = raw_html.replace(
            html_key,html_value
        )
        return implemented_html
