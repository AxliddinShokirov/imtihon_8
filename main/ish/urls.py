from django.urls import path
from . import views

urlpatterns = [
    path('staff-shift/', views.staff_shift_list, name='staff_shift_list'),
    path('staff-shift/create/', views.staff_shift_create, name='staff_shift_create'),
    path('staff-shift/<int:id>/update/', views.staff_shift_update, name='staff_shift_update'),
    path('staff-shift/<int:id>/delete/', views.staff_shift_delete, name='staff_shift_delete'),
    path('positionCraet/', views.positionCraet ,name='positionCraet'),
    path('positions/', views.positionList, name='positionList'),
    path('positions/delete/<int:pk>/', views.delete_position, name='PositionDelete'),
    path('positionUpdaet/<int:id>/', views.positionUpdate, name='positionUpdate')
]
