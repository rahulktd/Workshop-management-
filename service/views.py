from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from service.forms import WorkerForm, CustomerForm



#
#
# # Create your views here.
def start(request):
    return render(request, 'demo.html')
#
#
# home page
def Home(request):
    return render(request, 'car/Modified_files/index.html')
#
#
# login
@login_required
def Login(request):
    return render(request, 'Admin/Admin_dash.html')

# WORKER_LOGIN
@login_required
def Worker_Login(request):
    return render(request, 'WORKER_TEMPLATE/WORKER_DASH.html')

# USER_LOGIN
@login_required
def User_Login1(request):
    return render(request, 'USER_TEMPLATE/USER_DASH.html')

# dashboard
def dash(request):
    return render(request, 'car/dashboard/Modified_files/index.html')

# login setup
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('Login')
            elif user.is_worker:
                return redirect('Worker_Login')
            elif user.is_user:
                return redirect('User_Login1')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'car/Modified_files/login.html')

#registration form of worker
def worker_register(request):
    worker_form = WorkerForm()
    if request.method == 'POST':
        worker_form = WorkerForm(request.POST, request.FILES)
        if worker_form.is_valid():
            user = worker_form.save(commit=False)
            user.is_worker = True
            user.save()
            messages.info(request, 'Worker Registration Successful')
            return redirect('login_view')
    return render(request, 'WORKER_TEMPLATE/work_reg_form.html', {'worker_form': worker_form})

#registration form of customer
def customer_register(request):
    customer_form = CustomerForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES)
        if customer_form.is_valid():
            u = customer_form.save(commit=False)
            u.is_user = True
            u.save()
            messages.info(request, 'Customer Registration Successful')
            return redirect('login_view')
    return render(request, 'USER_TEMPLATE/customer_reg.html', {'customer_form': customer_form})

# # view workers
@login_required
def work_view(request):
    data = Login.objects.filter(is_worker=True)
    return render(request, 'WORKER_TEMPLATE/worker_view.html', {"data": data})


def signup(request):
    return render(request, 'signup_common.html')
#
@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

def details(request):
    data = Login.objects.all()
    return render(request, 'Admin/Admin_dash.html',{'data':data})



