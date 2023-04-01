from django.urls import path
from service import views, admin_view, customer_view

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
    path('signup',views.signup,name='signup'),


#admin
    path('admin_login',admin_view.admin_login,name='admin_login'),
    path('worker_view',admin_view.worker_view,name='worker_view'),
    path('customer_view',admin_view.customer_view,name='customer_view'),
    path('delete_customer/<int:id>/',admin_view.delete_customer,name='delete_customer'),
    path('delete_worker/<int:id>/',admin_view.delete_worker,name='delete_worker'),
    path('update_worker/<int:id>/',admin_view.update_worker,name='update_worker'),
    path('admin_feedback_view', admin_view.admin_feedback_view, name='admin_feedback_view'),
    path('reply_feedback/<int:id>/', admin_view.reply_feedback, name='reply_feedback'),
    path('admin_feedback_reply', admin_view.admin_feedback_reply, name='admin_feedback_reply'),


    #user
    path('customer_feedback', customer_view.customer_feedback, name='customer_feedback'),
    # path('feedback_view', customer_view.customer_feedback_view, name='feedback_view'),
    path('customer_feedback_view', customer_view.customer_feedback_view, name='customer_feedback_view'),



]
