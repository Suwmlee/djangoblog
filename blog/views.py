# Create your views here.
from django.template import loader, Context ,RequestContext
from django.http import HttpResponse
from blog.models import BlogPost
from linking.models import linking
from django.shortcuts import render_to_response

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

def test(request):
    links = linking.objects.all().order_by("-id")
    posts = BlogPost.objects.all().order_by("-timestamp")
    t = loader.get_template("test.html")
    c = Context({
                'posts': posts,
                 'links'  : links})
    return HttpResponse(t.render(c))

def show_post(request, pid):
    posts = BlogPost.objects.all().order_by("-timestamp")
    blog  = BlogPost.objects.get(id=pid)
    links = linking.objects.all().order_by("-id")
    #posts = BlogPost.objects.filter(id=int(pid))
    pid=int(pid)
    tflag=2;
    if pid==1:
        pre=1
        tflag=0
    else:
        pre=pid-1
    i=0
    for post in posts:
        i=i+1
    if pid>=i:
        pid=i
        nex=i
        tflag=1
    else:
        nex=pid+1
    pre = BlogPost.objects.get(id=pre)
    nex = BlogPost.objects.get(id=nex)
    t = loader.get_template("article.html")
    c = Context({ 'posts' : posts ,
                  'links' : links ,
                  'pre'   : pre   ,
                  'nex'   : nex   ,
                  'tflag' : tflag ,
                  'pid'   : pid})
    #return HttpResponse(t.render(c),)
    return render_to_response("article.html", {'posts':posts,'links':links,'pre':pre,'nex':nex,'pid':pid,'blog':blog,'tflag':tflag}, context_instance=RequestContext(request))

#def blog_show_comment(request, id=''):
    #blog = BlogPost.objects.get(id=id)
    #return render_to_response('blog_comments_show.html', {"blog": blog})

