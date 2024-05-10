from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('navbar/',views.Home,name='Home'),
    path('home/',views.count,name="index"),
    path('add_product/',views.new_product,name='add_product'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('add_deals/',views.add_deals,name="add_deals"),
    path('schedule_appointment/',views.appointment,name='appointment'),
    path('today_schedule/',views.todays_appointment,name="today_schedule"),
    path('view_products/', views.product_table, name='product_table'),
    path('',views.login_view,name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name="logout.html"),name='logout'),
    path('reset_password/',auth_view.PasswordResetView.as_view(template_name="password_reset.html"),name='reset_password'),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name='password_reset_complete'),
    
]