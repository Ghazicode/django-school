from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'home'
urlpatterns=[
    path('', views.HomeView.as_view(), name='main'),
    path('news', views.NewsView.as_view(), name='news'),
    path('news/detail/<str:search>', views.NewsDetailView.as_view(), name='news_detail'),
] 





urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)