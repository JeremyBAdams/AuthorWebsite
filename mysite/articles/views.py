from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.articles.article_response_builder import ArticleResponseBuilder

# Create your views here.
def index(request):
    arb = ArticleResponseBuilder(request)
    response = arb.get_index_response()
    return response


def article(request):
    arb = ArticleResponseBuilder(request)
    response = arb.get_article_response()
    return response
