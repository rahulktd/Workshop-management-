from django.contrib import messages
from django.shortcuts import render, redirect
from service import models
from service.forms import WorkerForm, SkillForm
from service.models import Login, Feedback, WorkerCategory


# from service.forms import WorkerForm, SkillForm
# from service.models import Worker, Customer, Feedback, WorkerCategory
#
#
def admin_login(request):
    return render(request,'Admin/Admin_dash.html')
#
def worker_view(request):
    data = Login.objects.filter(is_worker=True)
    return render(request, 'Admin/view_workers_list.html', {"data": data})
#
def customer_view(request):
    data = Login.objects.all()
    return render(request, 'Admin/view_customer_list.html', {"data": data})
#
def delete_customer(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect("customer_view")
#
def delete_worker(request, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect("worker_view")
#
def update_worker(request, id):
    worker = Login.objects.get(id=id)
    form = WorkerForm(instance=worker)
    if request.method == 'POST':
        form = WorkerForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_view')
    return render(request,'Admin/update_worker.html', {'form': form})
#
def admin_feedback_view(request):
    feedback=Feedback.objects.all()
    return render(request,'Admin/admin_feedback.html',{'feedback':feedback})
#
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
#
def accept_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("worker_view")
#
def reject_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("worker_view")
#
#
#
