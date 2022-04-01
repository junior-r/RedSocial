from re import template
import django
from django.urls import path
from .views import feed, profile, register, post, follow, unfollow
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', post, name='post'),
    path('follow/<str:username>/', follow, name='follow'),
    path('unfollow/<str:username>/', unfollow, name='unfollow'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
