from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]
