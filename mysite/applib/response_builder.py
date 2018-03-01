from django.http import HttpResponse
from applib.archetype import Archetype
from applib.client_tracker import ClientTracker
from applib.website_methods import *
from applib.author_website_keys import AuthorWebsiteKeys as awk

class ResponseBuilder:
    def __init__(self,request):
        """
        instantiate ResponseBuilder class

        Args:
            request (url): Django url object for page request

        Returns:
            None -> (instantitates ResponseBuilder class)
        """
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
            frontend_or_content (int): from AuthorWebsiteKeys, indicates
                whether the requested page is frontend code (HTML,CSS,JS),
                of website content (story articles, blog posts, etc.)

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
        frontend_or_content=awk.FRONTEND,  dependence=awk.PLATFORM_DEPENDENT,
        page="ws_skeleton"
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
            frontend_or_content (int): from AuthorWebsiteKeys, indicates whether
                the requested file is frontend code (HTML,CSS,JS) or website
                content (articles, blog posts, images, etc.)
            dependence (int): from AuthorWebsiteKeys, indicates whether the
                requested file is named based on client device (ie. .pc,
                .mobile, or .tablet), or if there is only one version of the
                file across all client device types
            page (string): title of the page as it sits in its directory
                (ie. no directory or file format extensions)

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
        """
        gets list of strings, each containing the contents of a single file
        in the provided file list

        Args:
            file_list (list)
                elem (string): path to a file

        Returns:
            (list)
                elem (string): contents of the requested file
        """
        return [self.get_file_contents(f) for f in file_list]

    def concatenate_file_content_strings(self, strings_list=None):
        """
        concatenates a list of strings from a file list

        Args:
            strings_list (list)
                elem (string): contents of a file
        Returns:
            (string): concatenated contents of all strings in submitted list
        """
        return "".join(strings_list)

    def stitch_and_get_page(
        self, title=None, all_css_L=None, all_body_html_L=None
    ):
        """
        creates a string representing a mature HTML(with CSS and JS) page
        for use with Django's HttpResponse

        Args:
            title (string): webpage title
            all_css_L (list)
                elem (string): string of CSS code for objects in output page
            all_body_html_L (list)
                elem (string): string of HTML for layout of objects in output
                    page
        Returns:
            (string): mature HTML page with associated title, HTML objects, and
                CSS objects
        """
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

    def get_coming_soon_html(self):
        """
        creates a mature page for features that are not yet developed

        Args:
            None

        Returns:
            (HttpResponse): coming soon page
        """
        title = "Coming Soon"

        global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
        header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
        footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
        archetype_css_path = self.get_page_path(
            app=awk.HOME, filetype=awk.CSS, page="warden"
        )
        all_css_L = self.get_file_contents_for_list(
            file_list=[global_css_path, header_css_path,
                       footer_css_path, archetype_css_path]
        )

        coming_soon_html_path = self.get_page_path(page="coming_soon")
        all_body_html_L = self.get_file_contents_for_list(
            file_list=[coming_soon_html_path]
        )

        implemented_html = self.stitch_and_get_page(
            title=title, all_css_L=all_css_L, all_body_html_L=all_body_html_L
        )

        return HttpResponse(implemented_html)

    def get_server_error_html(self):
        pass
