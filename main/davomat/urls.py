from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stafList, name='stafList'),
    path('UpdateStaf/<int:id>', views.update_Xodim, name='update_Xodim'),
    path('deleteStaf/<int:id>', views.StaffDelete, name='StaffDelete'),
    path('creatStaff/', views.staffCreate, name='staffCraet'),
    path('attendance/create/', views.create_Staffattendance, name='attendance_create'),

    path('attendance/', views.attendance, name='attendance'),
    path('create_Staffattendance/<int:id>', views.create_Staffattendance, name='create_Staffattendance'),
    path('update_attendance/<int:id>', views.update_attendance, name='update_attendance'),
    
    path('create_Staffattendance/', views.create_Staffattendance, name='create_Staffattendance'),
    path('delete_attendance/<int:id>', views.delete_attendance, name='delete_attendance'),

]
