from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import News





class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html', {})




class NewsView(View):
    def get(self, request):

        news = News.objects.filter(status = True)
        if s := request.GET.get('s'):
            news = news.filter(content__contains = s)
        special = news.filter(special = True)

        
        return render(request, 'home/news.html', {'news':news, 'special':special})
    



class NewsDetailView(View):
    def get(self, request, search):
        news = News.objects.get(status = True, search = search)
        news.views +=1
        news.save()
        
        return render(request, 'home/news-detail.html', {'news':news})
    



# class Like(View):
#     def get(self, request, search):
#         article = News.objects.get(status = True, search = search)
#         article.like +=1
#         article.save()
#         return redirect(f"/news/detail/{search}")