from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.news.news_response_builder import NewsResponseBuilder

# Create your views here.
def index(request):
    nrb = NewsResponseBuilder(request)
    response = nrb.get_index_response()
    return response
