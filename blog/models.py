from django.db import models
from accounts.models import User
from django_jalali.db import models as jmodels


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='News')
    title = models.CharField(max_length=255)
    content = models.TextField()
    subject = models.CharField(max_length=250)
    category = models.ManyToManyField('Category')
    tag = models.ManyToManyField('Tag')
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    search = models.CharField(max_length=250, unique=True)
    status = models.BooleanField(default=False)

    
    created_date = jmodels.jDateField(auto_now_add=True, verbose_name='زمان ثبت')
    updated_date = jmodels.jDateField(auto_now=True, verbose_name='زمان اپدیت')


    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title





class Category(models.Model):
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title
    




class Tag(models.Model):
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title
    



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.TextField()
    status = models.BooleanField(default=False)

    created_date = jmodels.jDateField(auto_now_add=True, verbose_name='زمان ثبت')
    


    def __str__(self):
        return self.name