from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models



class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'author', 'status', 'views')
    list_filter = ('status', 'title')
    search_fields = ('title', 'content')



admin.site.register(models.News, NewsAdmin)
