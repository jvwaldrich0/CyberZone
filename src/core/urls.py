# Django
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
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
from apps.users.views import user_home, register_request, logout_request
from apps.users.models import ExtendsUser

data  = {'blog':post,
         'forum':question,
         'user':ExtendsUser}


def home(request):
    return render(request, 'index.html', data)
def about(request):
    return render(request, 'about.html', data)
def login(request):
    return render(request, 'login.html')
    

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', about),
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('blog/', blog_home.as_view(), name='blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('forum/', forum_home.as_view(), name='forum'),
    path("logout", logout_request, name= "logout"),
    path("register", register_request, name="register"),
    path('user/home', user_home.as_view(), name='user_home'),
] + staticfiles_urlpatterns() + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)