from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article, Comments
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



class Blog(View):
    def get(self, request):
        articles = Article.objects.filter(status = True)
        if s := request.GET.get('s'):
            articles = articles.filter(content__contains = s)


        articles = Paginator(articles, 6)
        try:
            page_number = request.GET.get('page')
            articles = articles.get_page(page_number)
        except PageNotAnInteger:
            articles = articles.get_page(2)
        except EmptyPage:
            articles = articles.get_page(2)
            
            
        return render(request, 'blog/blog.html', {'articles':articles})
    


class BlogDetailView(View):
    def get(self, request, search):
        
        if not request.user.is_authenticated:
            return redirect(f'/account/login?next_page=/blog/detail/{search}')
        article = get_object_or_404(Article, status = True, search = search)
        article.views +=1
        article.save()
        comments = Comments.objects.filter(status = True, article = article)
        comments = Paginator(comments, 4)
        try:
            page_number = request.GET.get('page')
            comments = comments.get_page(page_number)
        except PageNotAnInteger:
            comments = comments.get_page(2)
        except EmptyPage:
            comments = comments.get_page(2)


        return render(request, 'blog/blog-detail.html', {'article':article, 'comments':comments})

    def post(self, request, search):
        if not request.user.is_authenticated:
            return redirect(f'/account/login?next_page=/blog/detail/{search}')
        else:
            user = request.user
            article_id = request.POST.get('article')
            name = request.POST.get('name')
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            article = get_object_or_404(Article, id = article_id, status = True )
            
            Comments.objects.create(
                author = user,
                article = article,
                name = name,
                email = email,
                comment = comment

            )
        return redirect(f'/blog/detail/{search}')
        
        