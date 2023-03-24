from django.contrib.auth import authenticate, login
# from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages


# from service.forms import LoginRegister, WorkerForm


from service.forms import LoginRegister, WorkerForm


# Create your views here.
def start(request):
    return render(request,'demo.html')

#home page
def Home(request):
    return render(request,'car/Modified_files/index.html')

#login
def Login(request):
    return render(request,'car/Modified_files/login.html')

#WORKER_LOGIN
def Worker_Login(request):
    return render(request,'WORKER_TEMPLATE/WORKER_DASH.html')

#USER_LOGIN
def User_Login(request):
    return render(request,'USER_TEMPLATE/USER_DASH.html')


#dashboard
def dash(request):
    return render(request,'car/dashboard/Modified_files/index.html')

#login setup
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('dash')
            elif user.is_worker:
                return redirect('Worker_Login')
            elif user.is_user:
                return redirect('User_Login')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'car/Modified_files/login.html')

def worker_register(request):
    user_form = LoginRegister()
    worker_form = WorkerForm()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        worker_form = WorkerForm(request.POST)
        if user_form.is_valid() and worker_form.is_valid():
            u = user_form.save(commit=False)
            u.is_worker = True
            u.save()
            worker = worker_form.save(commit=False)
            worker.user = u
            worker.save()
            messages.info(request, 'Worker Registration Successful')
            return redirect('login_view')
    return render(request, 'WORKER_TEMPLATE/work_reg_form.html', {'user_form': user_form, 'worker_form': worker_form})