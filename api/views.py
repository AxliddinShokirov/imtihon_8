from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status, permissions, authentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.models import Token
from main.models import Position, Shift, Staff, StaffShift, StaffAttendance
from .serializers import  *

class StaffListView(generics.ListCreateAPIView):
    serializer_class = StaffListSerializer
    queryset = Staff.objects.all()

class StaffAttendanceListView(generics.ListCreateAPIView):
    serializer_class = StaffAttendanceListSerializer
    queryset = StaffAttendance.objects.all()

class ShiftListView(generics.ListCreateAPIView):
    serializer_class = ShiftSerializer
    queryset = Shift.objects.all()

class StaffShiftListView(generics.ListCreateAPIView):
    serializer_class = StaffShiftListSerializer
    queryset = StaffShift.objects.all()

class PositionListView(generics.ListCreateAPIView):
    serializer_class = PositionListSerializer
    queryset = Position.objects.all()

class StaffAttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StaffAttendanceDetailSerializer
    queryset = StaffAttendance.objects.all()

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StaffDetailSerializer
    queryset = Staff.objects.all()

class PositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PositionDetailSerializer
    queryset = Position.objects.all()

@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        context = {
            'username': user.username,
            'key': token.key,
            'success': True,
        }
    else:
        context = {
            'success': False,
        }
    return Response(context)

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        context = {
            'username': user.username,
            'key': token.key,
            'success': True,
        }
    else:
        context = {
            'success': False,
        }
    return Response(context)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def log_out(request):
    user = request.user
    if user.is_authenticated:
        user.auth_token.delete()
        context = {'success': True}
    else:
        context = {'success': False}
    return Response(context)
