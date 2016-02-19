from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from blog.models import Blog
import datetime
def hello(request):
    return HttpResponse("hello world")

def now_date(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s.<body><html>" % now
    return HttpResponse(html)
def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html",{'blogs':blogs})
def blog_show(request,id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",{'blog':blog})

# Create your views here.
