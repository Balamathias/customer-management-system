from django.urls import path 

from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('account_setting/', views.account_setting, name='account-setting'),
    
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    
    path('logout/', views.log_out, name='logout'),
    path('user/', views.user, name='user'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('createorder/<str:pk>/', views.create_order, name='createorder'),
    path('updateorder/<str:pk>/', views.update_order, name='updateorder'),
    
    path('reset_password', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='reset_password'),
    
    path('reset_password_sent', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    
    
    # path('order/', views.order, name='order'),
    # path('order/addorder/', views.addorder, name='addorder'),
    
]
