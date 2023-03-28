from django.urls import path
from service import views, admin_view

urlpatterns = [
    path('start',views.start,name='start'),
    path('',views.Home,name='Home'),
    path('Login',views.Login,name='Login'),
    path('dash',views.dash,name='dash'),
    path('login_view',views.login_view,name='login_view'),
    path('Worker_Login',views.Worker_Login,name='Worker_Login'),
    path('User_Login1',views.User_Login1,name='User_Login1'),
    path('worker_register',views.worker_register,name='worker_register'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('work_view',views.work_view,name='work_view'),


#admin
    path('admin_login',admin_view.admin_login,name='admin_login'),
    path('worker_view',admin_view.worker_view,name='worker_view'),
    path('customer_view',admin_view.customer_view,name='customer_view'),
    path('delete_customer/<int:id>/',admin_view.delete_customer,name='delete_customer'),
    path('delete_worker/<int:id>/',admin_view.delete_worker,name='delete_worker'),
    path('update_worker/<int:id>/',admin_view.update_worker,name='update_worker'),

]
