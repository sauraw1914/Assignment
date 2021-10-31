from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
   path('post', views.PostCreateView, name="post"),
   path('success', views.success_msg, name="success"),
   path('<str:pk>/myposts/', views.myPosts, name="myposts"),
]