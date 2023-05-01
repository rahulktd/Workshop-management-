from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from service.forms import ScheduleForm, BillForm
from service.models import Schedule, Appointment, Bill

@login_required
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
@login_required
def view_schedules_worker(request):
    data = Schedule.objects.filter(worker=request.user)
    return render(request, 'WORKER_TEMPLATE/Scheduled_works_worker.html', {'data': data})
@login_required
def update_schedule(request, id):
    worker = Schedule.objects.get(id=id)
    form = ScheduleForm(instance=worker)
    if request.method == 'POST':
        form = ScheduleForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            return redirect('view_schedules_worker')
    return render(request,'WORKER_TEMPLATE/update_schedule.html', {'form': form})
@login_required
def delete_schedule(request, id):
    data = Schedule.objects.get(id=id)
    data.delete()
    return redirect("view_schedules_worker")
@login_required
def booked_app(request):
    data = Schedule.objects.filter(worker=request.user)
    app = Appointment.objects.filter(schedule__in = data)
    return render(request,'WORKER_TEMPLATE/bookings_worker.html',{'app':app})
@login_required
def approve_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("booked_app")
@login_required
def reject_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("booked_app")

# def approved_book(request):
#     accepted = Appointment.objects.filter(status=1)
#     return render(request, 'WORKER_TEMPLATE/approved_book.html', {'accepted':accepted})


# def create_invoice(request,id):
#     appointment = Appointment.objects.get(id=id)
#     worker = appointment.worker
#     if request.method == 'POST':
#         form = BillForm(request.POST)
#         if form.is_valid():
#             bill = form.save(commit=False)
#             bill.appointment = appointment
#             bill.worker = worker
#             bill.customer = appointment.worker
#             bill.save()
#             return redirect('booked_app')
#     else:
#         form = BillForm()
#     return render(request,'WORKER_TEMPLATE/create_invoice.html',{'form':form,'appointment':appointment})
@login_required
def create_invoice(request, id):
    appointment = Appointment.objects.get(id=id)
    worker = request.user
    if request.method == 'POST':
        description = request.POST['description']
        amount = request.POST['amount']
        invoice_date = request.POST['invoice_date']
        bill = Bill.objects.create(
            appointment=appointment,
            worker=worker,
            customer=appointment.worker,
            amount=amount,
            invoice_date=invoice_date
        )
        bill.save()
        return redirect('booked_app')
    return render(request, 'WORKER_TEMPLATE/create_invoice.html', {'appointment': appointment})
@login_required
def list_invoice(request):
    app = Appointment.objects.all()
    invoices = Bill.objects.all()
    return render(request, 'WORKER_TEMPLATE/invoices_list.html',{'app':app,'invoices':invoices})
@login_required
def requests_appproved(request):
    approved_bills = Bill.objects.filter(status=1)
    return render(request, 'WORKER_TEMPLATE/approved_list.html', {'approved_bills': approved_bills})

