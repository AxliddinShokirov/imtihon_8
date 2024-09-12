from django.shortcuts import render , redirect
from main import models
from django.contrib.auth.decorators import login_required

def index(request):
    
    return render(request, 'dashboard/base.html')




@login_required(login_url='login')
def attendance(request):
    attendance=models.StaffAttendance.objects.all()
    xodimlar=models.Staff.objects.all()
    redirect ('register_user')
    return render(request, 'dashboard/attendance.html', {'attendance': attendance, 'xodimlar': xodimlar})

def mark_attendance(request, id):
    attendance = models.StaffAttendance.objects.get(id=id)
    attendance.isinstance = not attendance.isinstance
    attendance.save()
    
    return redirect('attendance')

def Admins(request):
    admin =models.Admins.objects.last()
    return render(request, 'dashboard/base.html', {'admin': admin})
