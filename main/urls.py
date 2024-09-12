from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sss', views.index),
    path('', include('main.davomat.urls')),
    path('login/', include('main.login.urls')),
    path('attendesm/<int:id>/ ', views.mark_attendance, name='mark_attendance'),
    path('ish/', include('main.ish.urls')),
    path('admins/', views.Admins, name='admins'),
    path('api/', include('api.urls'))

]
