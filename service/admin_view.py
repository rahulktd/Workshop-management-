from django.shortcuts import render, redirect
from service import models
from service.forms import WorkerForm
from service.models import Worker, Customer, Feedback


def admin_login(request):
    return render(request,'Admin/Admin_dash.html')

def worker_view(request):
    data = Worker.objects.all()
    return render(request, 'Admin/view_workers_list.html', {"data": data})

def customer_view(request):
    data = Customer.objects.all()
    return render(request, 'Admin/view_customer_list.html', {"data": data})

def delete_customer(request, id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect("customer_view")

def delete_worker(request, id):
    data = Worker.objects.get(id=id)
    data.delete()
    return redirect("worker_view")

def update_worker(request, id):
    worker = Worker.objects.get(id=id)
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