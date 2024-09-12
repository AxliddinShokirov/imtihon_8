
from rest_framework import serializers
from main.models import Staff, StaffAttendance, Shift, Position, StaffShift

class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class StaffAttendanceListSerializer(serializers.ModelSerializer):
    staff = StaffListSerializer(read_only=True)
    class Meta:
        model = StaffAttendance
        fields = ['id', 'staff', 'date', 'isinstance']

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class StaffShiftListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'

class PositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class StaffAttendanceDetailSerializer(serializers.ModelSerializer):
    staff = StaffListSerializer(read_only=True)
    class Meta:
        model = StaffAttendance
        fields = ['id', 'staff', 'date', 'isinstance']

class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'l_name', 'f_name']

class PositionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'title']
