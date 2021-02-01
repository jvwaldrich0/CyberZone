# Django
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from django.shortcuts import render
from django.contrib import admin
# core
from core import settings
# blog
from apps.blog.views import blog_home
from apps.blog.models import post
# forum
from apps.forum.views import forum_home
from apps.forum.models import question
# users
from apps.users.views import user_home
from apps.users.models import ExtendsUser

data  = {'blog':post,
         'forum':question,
         'user':ExtendsUser}


def home(request):
    return render(request, 'index.html', data)
def about(request):
    return render(request, 'about.html', data)
def login(request):
    return render(request, 'login.html', data)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', blog_home.as_view(), name='blog'),
    path('forum/', forum_home.as_view(), name='forum'),
    path('user/home', user_home.as_view(), name='user_home'),
    path('login', login),
    path('', home),
    path('about/', about)
] + staticfiles_urlpatterns() + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)