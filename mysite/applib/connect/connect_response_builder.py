import os
import re
from django.http import HttpResponse
from applib.website_methods import *
from applib.response_builder import ResponseBuilder
from applib.archetype import Archetype
from applib.author_website_keys import AuthorWebsiteKeys as awk

class ConnectResponseBuilder(ResponseBuilder):

    def __init__(self, request):
        ResponseBuilder.__init__(self,request)

    def get_index_response(self):
        coming_soon_html = self.get_coming_soon_html()
        return HttpResponse(coming_soon_html)
