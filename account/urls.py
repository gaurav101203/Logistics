from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('login/', views.login_view, name='login'),
     path('user_login/', views.user_login, name='user_login'),
    path('choose/', views.choose, name='choose'),
     path('registration/', views.registration, name='registration'),
     path('company_login/', views.company_login, name='company_login'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
]