# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost
from linking.models import linking
def archive(request):
    links = linking.objects.all().order_by("-id")
    posts = BlogPost.objects.all().order_by("-timestamp")
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts,
                 'links'  : links})
    return HttpResponse(t.render(c))

def intro(request):
    links = linking.objects.all().order_by("-id")
    posts = BlogPost.objects.all().order_by("-timestamp")
    t = loader.get_template("intro.html")
    c = Context({ 'posts': posts,
                 'links'  : links})
    return HttpResponse(t.render(c))


def show_post(request, pid):
    #return HttpResponse(pid)
    posts = BlogPost.objects.all().order_by("-timestamp")
    links = linking.objects.all().order_by("-id")
    #posts = BlogPost.objects.filter(id=int(pid))
    pid=int(pid)
    t = loader.get_template("article.html")
    c = Context({ 'posts': posts,
                  'links': links,
                  'pid'  : pid})
    return HttpResponse(t.render(c))
