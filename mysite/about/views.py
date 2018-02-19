from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.about.about_response_builder import AboutResponseBuilder

# Create your views here.
def index(request):
    arb = AboutResponseBuilder(request)
    response = arb.get_index_response()
    return response
