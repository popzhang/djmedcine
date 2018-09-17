from django.db import models

# Create your models here.

class UserType(models.Model):
    """
    用户组
    """
    title = models.CharField(max_length=32)

    def __str__(self):
        return "%s-%s" % (self.id, self.title)

class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType',null=True,on_delete=models.SET_NULL)  # 设置外键
    password = models.CharField(max_length=16,default='')