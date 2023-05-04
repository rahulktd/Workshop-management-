from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect

from service.filters import WorkerFilter, CustomerFilter
from service.forms import WorkerForm, SkillForm, ScheduleForm, BillApprovalForm
from service.models import Login, Feedback, WorkerCategory, Schedule, Appointment, Bill, Payment

@login_required(login_url='/login_view/')
def admin_login(request):
    return render(request,'Admin/Admin_dash.html')
# @login_required(login_url='/login_view/')
# def worker_view(request):
#     data = Login.objects.filter(is_worker=True)
#     return render(request, 'Admin/view_workers_list.html', {"data": data})
@login_required(login_url='/login_view/')
def worker_view(request):
    worker_list = Login.objects.filter(is_worker=True)
    worker_filter = WorkerFilter(request.GET, queryset=worker_list)
    worker_list = worker_filter.qs
    return render(request, 'Admin/view_workers_list.html', {"worker_list": worker_list, "worker_filter": worker_filter})
# @login_required(login_url='/login_view/')
# def worker_view(request):
#     worker_filter = WorkerFilter(request.GET or None, queryset=Login.objects.filter(is_worker=True))
#     workers = worker_filter.qs
#     context = {
#         'workers': workers,
#         'worker_filter': worker_filter,
#     }
#     return render(request, 'Admin/view_workers_list.html', context)


# @login_required(login_url='/login_view/')
# def customer_view(request):
#     data = Login.objects.filter(is_user=True)
#     return render(request, 'Admin/view_customer_list.html', {"data": data})

@login_required(login_url='/login_view/')
def customer_view(request):
    customer_list = Login.objects.filter(is_user=True)
    customer_filter = CustomerFilter(request.GET, queryset=customer_list)
    customer_list = customer_filter.qs
    return render(request, 'Admin/view_customer_list.html', {"customer_list": customer_list, "customer_filter": customer_filter})

@login_required(login_url='/login_view/')
def delete_customer(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect("customer_view")
@login_required(login_url='/login_view/')
def delete_worker(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect("worker_view")
@login_required(login_url='/login_view/')
def update_worker(request, id):
    worker = Login.objects.get(id=id)
    form = WorkerForm(instance=worker)
    if request.method == 'POST':
        form = WorkerForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_view')
    return render(request,'Admin/update_worker.html', {'form': form})
@login_required(login_url='/login_view/')
def admin_feedback_view(request):
    feedback=Feedback.objects.all()
    return render(request,'Admin/admin_feedback.html',{'feedback':feedback})
@login_required(login_url='/login_view/')
def reply_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply=r
        feedback.save()
        messages.info(request,'Reply send')
        return redirect('admin_feedback_view')
    return render(request,'Admin/reply_feedback_admin.html',{'feedback':feedback})
@login_required(login_url='/login_view/')
def admin_feedback_reply(request):
    return render(request,'Admin/reply_feedback_admin.html')
@login_required(login_url='/login_view/')
def list_of_categories(request):
        categ = WorkerCategory.objects.all()
        return render(request, 'Admin/list_of_skills.html', {'categ': categ})
@login_required(login_url='/login_view/')
def skills_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_categories')
    else:
        form = SkillForm()
    return render(request,'Admin/admin_skills.html',{'form':form})
@login_required(login_url='/login_view/')
def accept_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("worker_view")
@login_required(login_url='/login_view/')
def reject_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("worker_view")
@login_required(login_url='/login_view/')
def view_work_admin(request):
    a = Schedule.objects.all()
    return render(request,'Admin/Scheduled_works.html',{'a':a})
@login_required(login_url='/login_view/')
def appointments_admin_view(request):
    accepted_appointments = Appointment.objects.filter(status=1)
    rejected_appointments = Appointment.objects.filter(status=2)
    return render(request, 'Admin/works_acc_rej.html', {'accepted_appointments': accepted_appointments, 'rejected_appointments': rejected_appointments})
@login_required(login_url='/login_view/')
def pending_invoice_requests(request):
    pending_bills = Bill.objects.filter(status=0)
    return render(request, 'Admin/pending_invoice_requests.html', {'pending_bills': pending_bills})

# def approve_invoice(request,id):
#     bill = Bill.objects.get(id=id)
#     if request.method == 'POST':
#         form = BillApprovalForm(request.POST, instance=bill)
#         if form.is_valid():
#             form.save()
#             return redirect('approved_invoice_requests')
#     else:
#         form = BillApprovalForm()
#     return render(request, 'Admin/invoice_approval.html',{'form':form, 'bill':bill})
@login_required(login_url='/login_view/')
def approved_invoice_requests(request):
    approved_bills = Bill.objects.filter(status=1)
    return render(request, 'Admin/approved_invoice_requests.html', {'approved_bills': approved_bills})
@login_required(login_url='/login_view/')
def approve_invoice(request,id):
    data = Bill.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("approved_invoice_requests")
@login_required(login_url='/login_view/')
def reject_invoice(request,id):
    data = Bill.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("pending_invoice_requests")
@login_required(login_url='/login_view/')
def payments_customer(request):
    payment = Payment.objects.filter(status=1)
    total_amount = payment.aggregate(Sum('amount_paid'))['amount_paid__sum']
    return render(request, 'Admin/history_of_pay.html', {'payment': payment,'total_amount': total_amount})

def view_worker_search(request):
    # a = Login.objects.filter(is_worker=True)
    # workerFilter = WorkerFilter(request.GET, queryset=a)
    # a = workerFilter.qs
    # context = {
    #     'worker':a,
    #     'workerFilter': workerFilter
    # }
    # return render(request,'Admin/view_workers_list.html',context)
    worker_list = Login.objects.filter(type='worker')
    worker_filter = WorkerFilter(request.GET, queryset=worker_list)
    worker_list = worker_filter.qs

    context = {
        'worker_list': worker_list,
        'worker_filter': worker_filter,
    }
    return render(request, 'Admin/view_workers_list.html', context)