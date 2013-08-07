# coding=utf-8
from django.contrib.syndication.views import Feed
from blog.models import BlogPost as Essay

class LatestEntriesFeed(Feed):
    #订阅标题
    title = u"更新"
    link = "/feeds/"
    #描述
    description = "关注最新动态"
    #订阅的数据
    def items(self):

    #posts = BlogPost.objects.all().order_by("-timestamp")
        return Essay.objects.order_by('-timestamp')[:5]
    #订阅的标题
    def item_title(self, item):
        return item.title
    #订阅的表示
    def item_description(self, item):
        return item.body
    #每条订阅的链接
    def item_link(self,item):
        return "/article/"+str(item.id)+"/"

