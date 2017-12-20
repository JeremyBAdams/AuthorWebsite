from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from applib.articles.article_manager import ArticleManager

am = ArticleManager()

css_dir = am.get_article_css_dir()
site_css = css_dir+"/site.css"

# Create your views here.
def index(request):
    response_string = """<!DOCTYPE HTML>
<head>
<link rel="stylesheet" type ="text/css" href="%s">
</head>
<body>
    <div class="my_div">
    Index page for articles app<br>
    static root is: %s<br>
    static url is: %s<br>
    css dir is: %s<br>
    warden css is: %s<br>
    rebel css is: %s<br>
    champion css is: %s<br>
    architect css is: %s<br>
    conqueror css is: %s<br>
    exile css is: %s<br>
    </div>
</body>
""" % (site_css,settings.STATIC_ROOT,settings.STATIC_URL,css_dir,
    am.get_archetype_css_file(am.WARDEN),
    am.get_archetype_css_file(am.REBEL),
    am.get_archetype_css_file(am.CHAMPION),
    am.get_archetype_css_file(am.ARCHITECT),
    am.get_archetype_css_file(am.CONQUEROR),
    am.get_archetype_css_file(am.EXILE)
)
    return HttpResponse(response_string)
