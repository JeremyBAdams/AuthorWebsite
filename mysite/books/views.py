from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.books.books_response_builder import BooksResponseBuilder

# Create your views here.
def index(request):
    brb = BooksResponseBuilder(request)
    response = brb.get_index_response()
    return response
