from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.connect.connect_response_builder import ConnectResponseBuilder

# Create your views here.
def index(request):
    crb = ConnectResponseBuilder(request)
    response = crb.get_index_response()
    return response
