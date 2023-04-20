from django.contrib import messages
from django.shortcuts import redirect, render

from service.forms import FeedbackForm, ScheduleForm, AppointmentForm
from service.models import Feedback, Schedule, Login, Appointment


def customer_feedback(request):
    feedback_form = FeedbackForm
    u = request.user
    if request.method=='POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            obj = feedback_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"Thank you for your feedback.")
            return redirect('customer_feedback_view')
    else:
        feedback_form = FeedbackForm
    return render(request,'USER_TEMPLATE/customer_feedback.html',{'feedback_form':feedback_form})

def customer_feedback_view(request):
    u = request.user
    feedback=Feedback.objects.filter(user=u)
    return render(request,'USER_TEMPLATE/customer_feedback_view.html',{'feedback':feedback})

def reply_view(request):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        reply_v = request.POST.get('reply')
        feedback.reply = reply_v
        feedback.save()
        return redirect('reply_view', id=id)
    else:
        form = FeedbackForm()
    return render(request, 'USER_TEMPLATE/customer_feedback_view.html', {'feedback': feedback})

def book_appointment(request,id):
    schedule = Schedule.objects.get(id=id)
    custo = Login.objects.get(name=request.user)
    app = Appointment.objects.filter(worker=custo,schedule=schedule)
    if app.exists():
        messages.info(request,"You have already requested ")
        return redirect('booking')
    else:
        if request.method == 'POST':
                obj = Appointment()
                obj.worker = custo
                obj.schedule = schedule
                obj.save()
                messages.info(request,'Appointment Booked ')
                return redirect('customer_bookings_view')
    return render(request,'USER_TEMPLATE/book_app.html',{'schedule':schedule})
def booking(request):
    data = Schedule.objects.all()
    return render(request,'USER_TEMPLATE/user_worker_schedule.html',{'data':data})

def customer_bookings_view(request):
    appointments = Appointment.objects.all()
    return render(request, 'USER_TEMPLATE/booking_history.html', {'appointments': appointments})

