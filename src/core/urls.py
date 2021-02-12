# django
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.urls import path, include
from django.shortcuts import render

from django.contrib import admin
# core
from core import settings
from core.auth.auth import register_request, logout_request, recovery_pwd, recovery_pwd_done
# blog
from apps.blog.views import blog_home, add_post, detail_blog, edit_post, delete_post
from apps.blog.models import post
# forum
from apps.forum.views import forum_home
from apps.forum.models import question
# users
from apps.users.views import user_home
from apps.users.models import ExtendsUser

data  = {'blog':post,
         'forum':question,
         'extendsuser':ExtendsUser}


def home(request):
    return render(request, 'home.html', data)
def about(request):
    return render(request, 'about.html', data)
def login(request):
    return render(request, 'sign_in_&&_sign_up.html')

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path("account/", register_request, name="account"),
    path("account/password_reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="reset_password"),
    path("account/password_reset_sent/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name="password_reset_done"),
    path("account/password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("account/password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    path('account/logout/',logout_request, name='logout'),
    path('admin/', admin.site.urls),
    path('blog/', blog_home.as_view(), name='blog'),
    path('blog/novo-artigo/', add_post.as_view(), name='novo_artigo'),
    path('blog/<slug:slug>', detail_blog.as_view(), name='detail_blog'),
    path('blog/edit/<slug:slug>', edit_post.as_view(), name='edit_post'),
    path('blog/delete/<slug:slug>', delete_post.as_view(), name='delete_post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('forum/', forum_home.as_view(), name='forum'),
    path('user/<int:pk>' , user_home.as_view(), name='user_home'),
] + staticfiles_urlpatterns() + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)