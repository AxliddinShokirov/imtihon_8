from django.core.exceptions import ObjectDoesNotExist
from main import models
from django.db import IntegrityError
from django.shortcuts import render , redirect
from django.db.models import Q 



def stafList(request):
    query = request.GET.get('q', '')
    staff = models.Staff.objects.filter(
        Q(l_name__icontains=query) |
        Q(f_name__icontains=query) |
        Q(email__icontains=query) |
        Q(phone_number__icontains=query) |
        Q(address__icontains=query)
    )

    context = {
        'staff': staff,
        'query': query
    }

    return render(request, 'dashboard/crude/xodim_list.html', context)




def staffCreate(request):
    context = {}
    context['categorys'] = models.Staff.objects.all()

    if request.method == 'POST':
        l_name = request.POST.get('l_name')
        f_name = request.POST.get('f_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

    
        if not all([l_name, f_name, age, email, phone, address]):
            context['error'] = "Barcha maydonlarni to'ldiring"
            return render(request, 'dashboard/staff/create.html', context)

        models.Staff.objects.create(
            l_name=l_name,
            f_name=f_name,
            age=age,
            email=email,
            phone_number=phone,  
            address=address
        )
        return redirect('stafList') 

    return render(request, 'dashboard/crude/xodim_craets.html', context)




def update_Xodim(request, id):
    xodim =models.Staff.objects.get(id=id)    
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')

        if not name:  
            return render(request, 'dashboard/crude/xodim_updeat.html', {
                'xodim': xodim,
                'error_message': 'Name field is required.'
            })

        try:
            xodim.name = name
            xodim.surname = surname
            xodim.age = age
            xodim.email = email
            xodim.phone_number = phone_number
            xodim.address = address
            xodim.save()
            return redirect('stafList')
        except IntegrityError as e:
            return render(request, 'Staff/xodim_updeat.html', {
                'xodim': xodim,
                'error_message': f' xatolik : {e}'
            })
    
    return render(request, 'dashboard/crude/xodim_updeat.html', {'xodim': xodim})


def StaffDelete(request, id):
    xodim = models.Staff.objects.get(id=id)
    xodim.delete()
    return redirect('stafList')


def create_Staffattendance(request):
    context = {}
    context['xodimlar'] = models.Staff.objects.all()

    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        date = request.POST.get('date')
        isinstance_value = request.POST.get('isinstance') in ['True', 'true', '1']

        if not staff_id or not date:
            context['error'] = "Xodim va sana maydonlari to'ldirilmagan"
            return render(request, 'dashboard/davomat/create.html', context)

        try:
            staff = models.Staff.objects.get(id=staff_id)
        except ObjectDoesNotExist:
            context['error'] = "Berilgan ID bo'yicha xodim topilmadi"
            return render(request, 'dashboard/davomat/create.html', context)

        if models.StaffAttendance.objects.filter(staff_id=staff_id, date=date).exists():
            context['error'] = "Ushbu sana bo'yicha ushbu xodim uchun davomat yozuvi allaqachon mavjud"
            return render(request, 'dashboard/davomat/create.html', context)

        models.StaffAttendance.objects.create(
            staff=staff,  
            date=date,
            isinstance=isinstance_value
        )
        return redirect('attendance_create')

    return render(request, 'dashboard/davomat/create.html', context)


def attendance(request):
    attendance = models.StaffAttendance.objects.all()
    return render(request, 'dashboard/attendance.html', {'attendance': attendance})



def update_attendance(request, id):
    attendance = models.StaffAttendance.objects.get(id=id)
    context = {}
    context['attendance'] = attendance
    context['xodimlar'] = models.Staff.objects.all()

    if request.method == 'POST':
        staff = models.Staff.objects.get(id=request.POST['xodim'])
        date = request.POST['date']
        isinstance_value = request.POST.get('isinstance', False) in ['True', 'true', '1']
        attendance.staff = staff
        attendance.date = date
        attendance.isinstance = isinstance_value
        attendance.save()
        return redirect('attendance')

    return render(request, 'dashboard/davomat/update.html', context)


    

def delete_attendance(request, id):
    attendance = models.StaffAttendance.objects.get(id=id)
    attendance.delete()
    return redirect('attendance')

    
