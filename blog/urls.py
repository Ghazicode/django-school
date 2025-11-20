from django.urls import path
from . import views

app_name = 'blog'
urlpatterns=[
    path('', views.Blog.as_view(), name='main'),
    path('detail/<str:search>', views.BlogDetailView.as_view(), name='detail')


]