from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import News
import jdatetime




class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html', {})




class NewsView(View):
    def get(self, request):
        now_jalali = jdatetime.datetime.now()
        # News.objects.filter(exp_date__lte=now_jalali).delete()
        news = News.objects.filter(status = True, exp_date__gt=now_jalali)
        special = news.filter(special = True)

        
        return render(request, 'home/news.html', {'news':news, 'special':special})
    



class NewsDetailView(View):
    def get(self, request, search):
        news = News.objects.get(status = True, search = search)
        
        return render(request, 'home/news-detail.html', {'news':news})
    



# class Like(View):
#     def get(self, request, search):
#         article = News.objects.get(status = True, search = search)
#         article.like +=1
#         article.save()
#         return redirect(f"/news/detail/{search}")