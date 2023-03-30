from django.contrib.auth import authenticate, login
# from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages



# from service.forms import LoginRegister, WorkerForm


from service.forms import LoginRegister, WorkerForm, CustomerForm
from service.models import Worker


# Create your views here.
def start(request):
    return render(request,'demo.html')

#home page
def Home(request):
    return render(request,'car/Modified_files/index.html')

#login
def Login(request):
    return render(request,'Admin/Admin_dash.html')

#WORKER_LOGIN
def Worker_Login(request):
    return render(request,'WORKER_TEMPLATE/WORKER_DASH.html')

#USER_LOGIN
def User_Login1(request):
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
        print(user)
        if user is not None:
            login(request, user)
            print(user)
            if user.is_staff:
                print(user)
                return redirect('Login')
            elif user.is_worker:
                print(user)
                return redirect('Worker_Login')
            elif user.is_user:
                # print(user)
                return redirect('User_Login1')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'car/Modified_files/login.html')

def worker_register(request):
    user_form = LoginRegister()
    worker_form = WorkerForm()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST,)
        worker_form = WorkerForm(request.POST,request.FILES)
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

def customer_register(request):
    user_form = LoginRegister()
    customer_form = CustomerForm()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST,)
        customer_form = CustomerForm(request.POST,request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            u = user_form.save(commit=False)
            u.is_user = True
            u.save()
            customer = customer_form.save(commit=False)
            customer.user = u
            customer.save()
            messages.info(request, 'Customer Registration Successful')
            return redirect('login_view')
    return render(request, 'USER_TEMPLATE/customer_reg.html', {'user_form': user_form, 'customer_form': customer_form})

#view workers
def work_view(request):
    data = Worker.objects.all()
    return render(request, 'WORKER_TEMPLATE/worker_view.html', {"data": data})

def signup(request):
    return render(request,'signup_common.html')