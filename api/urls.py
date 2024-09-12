from django.urls import path
from .views import *

urlpatterns = [
  
    path('staff/', StaffListView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('attendance/', StaffAttendanceListView.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', StaffAttendanceDetailView.as_view(), name='attendance-detail'),
    path('shifts/', ShiftListView.as_view(), name='shift-list'), 
    path('staff-shifts/', StaffShiftListView.as_view(), name='staff-shift-list'),  
    path('positions/', PositionListView.as_view(), name='position-list'),
    path('positions/<int:pk>/', PositionDetailView.as_view(), name='position-detail'),   
    path('login/', log_in, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', log_out, name='logout'),
    ]
