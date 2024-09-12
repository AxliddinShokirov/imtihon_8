
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from main import models 


def positionList(request):
    query = request.GET.get('q', '')
    if query:
        positions = models.Position.objects.filter(title__icontains=query)
    else:
        positions = models.Position.objects.all()
    return render(request, 'Position/position_list.html', {'positions': positions, 'query': query})

def delete_position(request, pk):
    position = get_object_or_404(models.Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('positionList')
    return render(request, 'Position/confirm_delete.html', {'position': position})


def positionCraet(request):
    context = {}
    context['positions'] = models.Position.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        if not all([title]):
            context['error'] = "Barcha maydonlarni to'ldiring"
            return render(request, 'position_create.html', context)
        models.Position.objects.create(title=title)
        return redirect('positionList')
    return render(request, 'Position/positioncraet.html', context)



def positionUpdate(request, id):
    position = models.Position.objects.get(id=id)
    context = {'position': position}
    if request.method == 'POST':
        title=request.POST.get('title')
        if not all([title]):
            context['error'] = "Barcha maydonlarni to'ldiring"
            return render(request, 'Position/update_position.html', context)
        position.title = title
        position.save()
        return redirect('positionList')
    return render(request, 'Position/update_position.html', context)


def positionDelete(request, id):
    position = models.Position.objects.get(id=id)
    position.delete()
    return redirect('positionList')



def shiftList(request):
    shifts = models.Shift.objects.all()
    return render(request, 'dashboard/shift_list.html', {'shifts': shifts})



def shiftCreate(request):
    context={}
    context['positions'] = models.Shift.objects.all()
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        models.Shift.objects.create(
             start_time=start_time,
             end_time=end_time,
    
                    )
        return redirect('shiftList')
    return render(request, 'dashboard/shift_create.html', context)



def staff_shift_list(request):
    staff_shifts = models.StaffShift.objects.all()
    return render(request, 'dashboard/ish/staff_shift_list.html', {'staff_shifts': staff_shifts})



def staff_shift_create(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        position_id = request.POST.get('position')
        shift_id = request.POST.get('shift')

        try:
            staff = models.Staff.objects.get(id=staff_id)
            position = models.Position.objects.get(id=position_id)
            shift = models.Shift.objects.get(id=shift_id)
        except models.Staff.DoesNotExist or models.Position.DoesNotExist or models.Shift.DoesNotExist:
            return render(request, 'dashboard/ish/staff_shift_list.html')

        models.StaffShift.objects.create(
            staff=staff,
            position=position,
            shift=shift
        )
        return redirect('staff_shift_list')
    
    context = {
        'staff_list': models.Staff.objects.all(),
        'position_list': models.Position.objects.all(),
        'shift_list': models.Shift.objects.all()
    }
    return render(request, 'dashboard/ish/staff_shift_create.html', context)



def staff_shift_update(request, id):
    staff_shift = get_object_or_404(models.StaffShift, id=id)

    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        position_id = request.POST.get('position')
        shift_id = request.POST.get('shift')

        try:
            staff = models.Staff.objects.get(id=staff_id)
            position = models.Position.objects.get(id=position_id)
            shift =models.Shift.objects.get(id=shift_id)
        except ObjectDoesNotExist:
            return render(request, 'dashboard/ish/staff_shift_form.html', {'error': 'Invalid data'})
        
        staff_shift.staff = staff
        staff_shift.position = position
        staff_shift.shift = shift
        staff_shift.save()
        return redirect('staff_shift_list')

    context = {
        'staff_shift': staff_shift,
        'staff_list':models.Staff.objects.all(),
        'position_list': models.Position.objects.all(),
        'shift_list': models.Shift.objects.all()
    }
    return render(request, 'dashboard/ish/staff_shift_form.html', context)


def staff_shift_delete(request, id):
    staff_shift = get_object_or_404(models.StaffShift, id=id)
    if request.method == 'POST':
        staff_shift.delete()
        return redirect('staff_shift_list')
    return render(request, 'dashboard/ish/staffdelete.html', {'staff_shift': staff_shift})
