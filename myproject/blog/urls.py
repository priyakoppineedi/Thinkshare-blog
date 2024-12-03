from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostUpdateView
from .views import PostDeleteView
from .views import profile
from .views import profile_update
from blog.views import CustomPasswordChangeView
from .views import like_post


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    
    
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('post/new/', views.post_create, name='post-create'),

    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile, name='profile'),

    path('register/', views.register, name='register'), 

    path('profile/update/', views.profile_update, name='profile-update'),
    
    path('profile/change-password/', CustomPasswordChangeView.as_view(), name='change-password'),

    
    path('post/<int:pk>/like/', views.like_post, name='like-post'),

]

