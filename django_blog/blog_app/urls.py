from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path("",views.blog_list,name='blog_list'),
    path("post/<int:pk>/", views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('post/<int:pk>/delete/',views.post_delete,name='post_delete'),
    path('register/',views.register,name='register'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),

    path('reset_password/',auth_view.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='reset_password'),

    path('reset_password_send/',auth_view.PasswordResetDoneView.as_view(template_name='registration/password_reset_send.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),

    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),

]