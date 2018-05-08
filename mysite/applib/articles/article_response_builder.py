import os
import re
from articles.models import Article, Pseudonym, Series
from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype
from applib.author_website_keys import AuthorWebsiteKeys as awk

class ArticleResponseBuilder(ResponseBuilder):

    def __init__(self,request):
        ResponseBuilder.__init__(self,request)

    def get_index_response(self):
        title = "Stories of Blessed Astra"

        global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
        header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
        footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
        index_css_path = self.get_page_path(
            app=awk.ARTICLES, filetype=awk.CSS, page="index"
        )
        archetype_css_path = self.get_page_path(
            app=awk.ARTICLES, filetype=awk.CSS, page="warden")
        all_css_L = self.get_file_contents_for_list(
            [global_css_path, header_css_path, footer_css_path,
            index_css_path, archetype_css_path]
        )
        index_js_path = self.get_page_path(
            app=awk.ARTICLES, filetype=awk.JS, path_or_url=awk.STATICURL,
            dependence=awk.PLATFORM_INDEPENDENT, page="article_index_functions"
        )
        all_js_L = [index_js_path]

        index_html_path = self.get_page_path(
            app=awk.ARTICLES, page="article_index"
        )
        all_body_html_L = self.get_file_contents_for_list(
            file_list=[index_html_path]
        )

        print(index_js_path)
        implemented_html = self.stitch_and_get_page(
            title=title, all_css_L=all_css_L, all_body_html_L=all_body_html_L, all_js_L=all_js_L
        )

        return HttpResponse(implemented_html)

    def get_mature_article_css(self, url_string=None, article_obj=None):
        article_response_css_path = self.get_page_path(
            app=awk.ARTICLES, filetype=awk.CSS, page="response"
        )
        article_response_css = self.get_file_contents(
            article_response_css_path
        )
        article_bg_image_path = self.get_page_path(
            app=awk.ARTICLES, filetype = awk.JPG, path_or_url=awk.STATICURL,
            page=url_string, frontend_or_content=awk.CONTENT
        )
        article_bg_image_path = article_bg_image_path.replace("//", "/")
        print(article_bg_image_path)

        mature_response_css = article_response_css\
            .replace("ARTICLE_VAR_BG_IMAGE",article_bg_image_path)

        return mature_response_css

    def get_mature_article_html(self, url_string=None, article_obj=None):
        title = article_obj.title
        date = article_obj.pub_date
        formatted_date = date.strftime("%B %d, %Y")

        pseudonym_obj = Pseudonym.objects.get(pseudonym_id=article_obj.pseudonym_id)
        pseudonym = pseudonym_obj.pseudonym

        series_obj = Series.objects.get(series_id=article_obj.series_id)
        series_name = series_obj.series_name

        article_skeleton_path = self.get_page_path(
            app=awk.ARTICLES, page="article_response"
        )
        article_skeleton_html = self.get_file_contents(
            path=article_skeleton_path
        )

        article_content_path = self.get_page_path(
            app=awk.ARTICLES, frontend_or_content=awk.CONTENT,
            page=url_string
        )
        article_content_html = self.get_file_contents(
            path=article_content_path
        )

        mature_article_html = article_skeleton_html\
            .replace("ARTICLE_TITLE",title)\
            .replace("ARTICLE_PSEUDONYM",pseudonym)\
            .replace("ARTICLE_SERIES",series_name)\
            .replace("ARTICLE_CONTENT",article_content_html)\
            .replace("ARTICLE_DATE",formatted_date)

        return mature_article_html

    def get_article_response(self):
        url_string = self.request.path.split("/")[-1]
        article_obj = Article.objects.get(url_string=url_string)

        if article_obj:
            title = article_obj.title
            description = article_obj.description

            global_css_path = self.get_page_path(filetype=awk.CSS, page="global")
            header_css_path = self.get_page_path(filetype=awk.CSS, page="ws_header")
            footer_css_path = self.get_page_path(filetype=awk.CSS, page="ws_footer")
            archetype_css_path = self.get_page_path(
                app=awk.ARTICLES, filetype=awk.CSS, page="warden")

            mature_article_css = self.get_mature_article_css(
                url_string=url_string, article_obj=article_obj
            )

            all_css_L = self.get_file_contents_for_list(
                [global_css_path, header_css_path, footer_css_path,
                archetype_css_path]
            )
            all_css_L.append(mature_article_css)

            mature_article_html = self.get_mature_article_html(
                url_string=url_string, article_obj=article_obj
            )
            all_body_html_L = [mature_article_html]

            implemented_html = self.stitch_and_get_page(
                title=title, description=description, all_css_L=all_css_L,
                all_body_html_L=all_body_html_L
            )

        return HttpResponse(implemented_html)
