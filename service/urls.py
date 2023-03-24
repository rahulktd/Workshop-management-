from django.urls import path
from service import views

urlpatterns = [
    path('start',views.start,name='start'),
    path('',views.Home,name='Home'),
    path('Login',views.Login,name='Login'),
    path('dash',views.dash,name='dash'),
    path('login_view',views.login_view,name='login_view'),
    path('Worker_Login',views.Worker_Login,name='Worker_Login'),
    path('User_Login',views.User_Login,name='User_Login'),
    path('worker_register',views.worker_register,name='worker_register'),
]