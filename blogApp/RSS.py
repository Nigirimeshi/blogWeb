from django.contrib.syndication.views import Feed

from .models import Post

class RssFeed(Feed):
    title = "Huaji 博客"
    link = "120.79.74.148/RSS/"
    description = "个人博客"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return "标题: %s" % (item.title)

    def item_description(self, item):
        return item.body