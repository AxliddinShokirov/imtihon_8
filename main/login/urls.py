from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_user, name='register_user'),  
    path('', views.login_user, name='login_user'),  
    path('logout/', views.log_out, name='log_out'),  
    path('error/', views.error, name='error'), 
]