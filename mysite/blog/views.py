from django.shortcuts import render
from django.http import HttpResponse
from applib.blog.blog_response_builder import BlogResponseBuilder

# Create your views here.
def index(request):
    brb = BlogResponseBuilder(request)
    response = brb.get_coming_soon_html()
    return response
