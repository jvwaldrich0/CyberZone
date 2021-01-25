from django.conf.urls.static import static
from django.urls import path, include
from apps.blog.views import blog_home
from django.shortcuts import render
from django.contrib import admin
from core import settings

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', blog_home.as_view(), name='home'),
    path('', home),
] + static(settings.STATIC_URL, 
           document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT
)
