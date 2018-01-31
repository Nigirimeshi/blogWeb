from haystack import indexes
from .models import Post, Category, Tag


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """
    * 创建 Post 索引
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
