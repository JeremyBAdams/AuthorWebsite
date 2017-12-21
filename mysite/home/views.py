from django.shortcuts import render
from django.http import HttpResponse

from applib.home.home_response_builder import HomeResponseBuilder

# Create your views here.
def index(request):
    """index page view for home app"""
    hrb = HomeResponseBuilder(request)
    response = hrb.get_index_response()
    return response
