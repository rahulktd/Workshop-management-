from django.urls import path
from service import views, admin_view, customer_view, worker_view

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
    path('logout_view',views.logout_view,name='logout_view'),



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
    path('list_of_categories', admin_view.list_of_categories, name='list_of_categories'),
    path('skills_add', admin_view.skills_add, name='skills_add'),
    path('accept_worker/<int:id>/', admin_view.accept_worker, name='accept_worker'),
    path('reject_worker/<int:id>/', admin_view.reject_worker, name='reject_worker'),
    # path('work_schedule',admin_view.work_schedule,name='work_schedule'),
    # path('view_work_schedule',admin_view.view_work_schedule,name='view_work_schedule'),
    path('view_work_admin',admin_view.view_work_admin,name='view_work_admin'),
    path('appointments_admin_view',admin_view.appointments_admin_view,name='appointments_admin_view'),
    # path('approve_invoice/<int:id>/',admin_view.approve_invoice,name='approve_invoice'),
    path('pending_invoice_requests',admin_view.pending_invoice_requests,name='pending_invoice_requests'),
    path('approved_invoice_requests',admin_view.approved_invoice_requests,name='approved_invoice_requests'),
    path('approve_invoice/<int:id>/',admin_view.approve_invoice,name='approve_invoice'),
    path('reject_invoice/<int:id>/',admin_view.reject_invoice,name='reject_invoice'),

    #user
    path('customer_feedback', customer_view.customer_feedback, name='customer_feedback'),
    # path('feedback_view', customer_view.customer_feedback_view, name='feedback_view'),
    path('customer_feedback_view', customer_view.customer_feedback_view, name='customer_feedback_view'),
    path('book_appointment/<int:id>/', customer_view.book_appointment, name='book_appointment'),
    path('booking', customer_view.booking, name='booking'),
    path('customer_bookings_view', customer_view.customer_bookings_view, name='customer_bookings_view'),
    path('invoices', customer_view.invoices, name='invoices'),
    path('pay_now/<int:id>/', customer_view.pay_now, name='pay_now'),
    path('pay_opt', customer_view.pay_opt, name='pay_opt'),


    #worker
    # path('view_work_times', worker_view.view_work_times, name='view_work_times'),
    path('schedule', worker_view.schedule, name='schedule'),
    path('view_schedules_worker', worker_view.view_schedules_worker, name='view_schedules_worker'),
    path('delete_schedule/<int:id>/',worker_view.delete_schedule,name='delete_schedule'),
    path('update_schedule/<int:id>/',worker_view.update_schedule,name='update_schedule'),
    path('booked_app',worker_view.booked_app,name='booked_app'),
    path('approve_booking/<int:id>/', worker_view.approve_booking, name='approve_booking'),
    path('reject_booking/<int:id>/', worker_view.reject_booking, name='reject_booking'),
    path('create_invoice/<int:id>/', worker_view.create_invoice, name='create_invoice'),
    path('list_invoice', worker_view.list_invoice, name='list_invoice'),
    path('requests_appproved', worker_view.requests_appproved, name='requests_appproved'),
    # path('approved_book', worker_view.approved_book, name='approved_book'),

]
