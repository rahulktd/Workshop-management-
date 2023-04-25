from django.contrib import messages
from django.shortcuts import render, redirect
from service.forms import WorkerForm, SkillForm, ScheduleForm, BillApprovalForm
from service.models import Login, Feedback, WorkerCategory, Schedule, Appointment, Bill


def admin_login(request):
    return render(request,'Admin/Admin_dash.html')

def worker_view(request):
    data = Login.objects.filter(is_worker=True)
    return render(request, 'Admin/view_workers_list.html', {"data": data})

def customer_view(request):
    data = Login.objects.filter(is_user=True)
    return render(request, 'Admin/view_customer_list.html', {"data": data})

def delete_customer(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect("customer_view")

def delete_worker(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect("worker_view")

def update_worker(request, id):
    worker = Login.objects.get(id=id)
    form = WorkerForm(instance=worker)
    if request.method == 'POST':
        form = WorkerForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_view')
    return render(request,'Admin/update_worker.html', {'form': form})

def admin_feedback_view(request):
    feedback=Feedback.objects.all()
    return render(request,'Admin/admin_feedback.html',{'feedback':feedback})

def reply_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply=r
        feedback.save()
        messages.info(request,'Reply send')
        return redirect('admin_feedback_view')
    return render(request,'Admin/reply_feedback_admin.html',{'feedback':feedback})

def admin_feedback_reply(request):
    return render(request,'Admin/reply_feedback_admin.html')
def list_of_categories(request):
        categ = WorkerCategory.objects.all()
        return render(request, 'Admin/list_of_skills.html', {'categ': categ})

def skills_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_categories')
    else:
        form = SkillForm()
    return render(request,'Admin/admin_skills.html',{'form':form})

def accept_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("worker_view")

def reject_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("worker_view")

def view_work_admin(request):
    a = Schedule.objects.all()
    return render(request,'Admin/Scheduled_works.html',{'a':a})

def appointments_admin_view(request):
    accepted_appointments = Appointment.objects.filter(status=1)
    rejected_appointments = Appointment.objects.filter(status=2)
    return render(request, 'Admin/works_acc_rej.html', {'accepted_appointments': accepted_appointments, 'rejected_appointments': rejected_appointments})

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

def approved_invoice_requests(request):
    approved_bills = Bill.objects.filter(status=1)
    return render(request, 'Admin/approved_invoice_requests.html', {'approved_bills': approved_bills})

def approve_invoice(request,id):
    data = Bill.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("approved_invoice_requests")

def reject_invoice(request,id):
    data = Bill.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("pending_invoice_requests")