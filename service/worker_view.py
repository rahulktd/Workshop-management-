from django.shortcuts import render, redirect

from service.forms import ScheduleForm
from service.models import Schedule, Appointment


# def view_work_times(request):
#     scheduled_works = WorkSchedule.objects.filter(worker=request.user)
#     return render(request, 'WORKER_TEMPLATE/Scheduled_works_worker.html', {'scheduled_works': scheduled_works} )

def schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.worker = request.user
            schedule.save()
            return redirect('view_schedules_worker')
    else:
        form = ScheduleForm()
    return render(request, 'WORKER_TEMPLATE/schedule.html', {'form': form})

def view_schedules_worker(request):
    u = request.user
    data = Schedule.objects.filter(worker=request.user)
    return render(request, 'WORKER_TEMPLATE/Scheduled_works_worker.html', {'data': data})

def update_schedule(request, id):
    worker = Schedule.objects.get(id=id)
    form = ScheduleForm(instance=worker)
    if request.method == 'POST':
        form = ScheduleForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            return redirect('view_schedules_worker')
    return render(request,'WORKER_TEMPLATE/update_schedule.html', {'form': form})

def delete_schedule(request, id):
    data = Schedule.objects.get(id=id)
    data.delete()
    return redirect("view_schedules_worker")

def booked_app(request):
    app = Appointment.objects.all()
    return render(request,'WORKER_TEMPLATE/bookings_worker.html',{'app':app})

def approve_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("booked_app")

def reject_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("booked_app")

