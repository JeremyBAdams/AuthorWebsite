from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.archetype import Archetype
from applib.client_tracker import ClientTracker
from applib.articles.article_response_builder import ArticleResponseBuilder

archetype = Archetype()
client_tracker = ClientTracker()
article_manager = ArticleResponseBuilder()

# Create your views here.
def index(request):
    cssfile = article_manager.get_archetype_css_file(archetype.WARDEN)
    response_string = """<!DOCTYPE HTML>
<head>
<link rel="stylesheet" type ="text/css" href="%s">
</head>
<body>
    <div class="my_div">
    Index page for articles app<br>
    Welcome Friendo<br><br>
    </div>
</body>
""" % (cssfile)

    return HttpResponse(response_string)

def article(request):
    pass
