from django.db import models
from ckeditor.fields import RichTextField

# Create your models here
class Catalog(models.Model):
    """
    文章分类目录
    """
    cataID = models.CharField(verbose_name=u"分类代码",max_length=16)
    name = models.CharField(verbose_name=u"分类名称",max_length=32)
    upperID = models.CharField(verbose_name=u"上级分类代码",max_length=16)
    mod_date = models.DateTimeField(verbose_name=u'最后修改日期', auto_now = True)


    # def __str__(self):
    #     return "%s-%s" % (self.id, self.title)

class Article(models.Model):
    """
    文章列表
    """
    articleID = models.CharField(verbose_name=u"文章代码",max_length=16)
    cataID = models.CharField(verbose_name=u"分类代码",max_length=16)
    name = models.CharField(verbose_name=u"文章标题",max_length=64)
    name2 = models.CharField(verbose_name=u"文章副标题",max_length=64)
    author = models.CharField(verbose_name=u"文章作者",max_length=16)
    time = models.DateField(verbose_name=u"发表时间",max_length=16)
    content = models.TextField(verbose_name=u"文章内容")
    art_body = RichTextField(blank=True,null=True,verbose_name="内容")
    mod_date = models.DateTimeField(verbose_name=u'最后修改日期', auto_now = True)
