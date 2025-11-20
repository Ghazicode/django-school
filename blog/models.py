from django.db import models
from accounts.models import User
from django_jalali.db import models as jmodels


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    subject = models.CharField(max_length=250, verbose_name='موضوع')
    categorys = models.ManyToManyField('Category', related_name='articles', verbose_name='دسته بندی‌‌ها')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='تگ ها')
    like = models.IntegerField(default=0, verbose_name='لایک')
    views = models.IntegerField(default=0, verbose_name='بازدید')
    read = models.IntegerField(default=0, verbose_name='زمان خواندن')
    search = models.CharField(max_length=250, unique=True, verbose_name='ادرس')
    status = models.BooleanField(default=False, verbose_name='وضعیت')

    
    created_date = jmodels.jDateField(auto_now_add=True, verbose_name='زمان ثبت')
    updated_date = jmodels.jDateField(auto_now=True, verbose_name='زمان اپدیت')


    class Meta:
        ordering = ("-id",)
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        

    def __str__(self):
        return self.title





class Category(models.Model):
    title = models.CharField(unique=True, max_length=250, verbose_name='عنوان')
    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "دسته‌بندی‌"
        verbose_name_plural = "دسته‌بندی‌ها"
    




class Tag(models.Model):
    title = models.CharField(unique=True, max_length=250, verbose_name='عنوان')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ‌ها"

    



class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='نویسنده')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    name = models.CharField(max_length=250, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    comment = models.TextField(verbose_name='نظر')
    status = models.BooleanField(default=False, verbose_name='وضعیت')

    created_date = jmodels.jDateField(auto_now_add=True, verbose_name='زمان ثبت')

    
    class Meta:
        ordering = ("-id",)
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return self.name