from django.db import models
from accounts.models import User
from django_jalali.db import models as jmodels





class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news', verbose_name='نویسنده')
    title = models.CharField(max_length=250, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='news', verbose_name='عکس')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    read = models.IntegerField(default=0, verbose_name='زمان خواندن')
    views = models.IntegerField(default=0, verbose_name='بازدید')
    like = models.IntegerField(default=0, verbose_name='لایک')
    search = models.CharField(max_length=250, verbose_name='ادرس')
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    special = models.BooleanField(default=False, verbose_name='ویژه')

    
    created_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name='اپدیت')
    updated_date = jmodels.jDateTimeField(auto_now=True, verbose_name='اپدیت')
    published_date = jmodels.jDateTimeField(verbose_name='تاریخ انتشار')
    exp_date = jmodels.jDateTimeField(verbose_name='تاریخ انقضا')



    class Meta:
        ordering = ("-id",)
        verbose_name = "خبر"
        verbose_name_plural = "خبر‌ها‌"
        


    def __str__(self):
        return self.title