from io import BytesIO

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from reportlab.pdfgen import canvas

from service.forms import FeedbackForm, PaymentForm
from service.models import Feedback, Schedule, Login, Appointment, Bill, Payment

@login_required
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
@login_required
def customer_feedback_view(request):
    u = request.user
    feedback=Feedback.objects.filter(user=u)
    return render(request,'USER_TEMPLATE/customer_feedback_view.html',{'feedback':feedback})
@login_required
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
@login_required
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
@login_required
def booking(request):
    data = Schedule.objects.all()
    return render(request,'USER_TEMPLATE/user_worker_schedule.html',{'data':data})
@login_required
def customer_bookings_view(request):
    appointments = Appointment.objects.filter(worker=request.user)
    return render(request, 'USER_TEMPLATE/booking_history.html', {'appointments': appointments})
@login_required
def invoices(request):
    approved_bills = Bill.objects.filter(customer=request.user,status=1)
    return render(request, 'USER_TEMPLATE/invoice.html', {'approved_bills': approved_bills})
@login_required
def pay_now(request,id):
    bill = Bill.objects.get(id=id)
    appointment = bill.appointment
    form = PaymentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if Payment.objects.filter(bill=bill, customer=request.user).exists():
                messages.warning(request, 'You have already made a payment for this bill.')
                return redirect('pay_opt')
            payment = form.save(commit=False)
            payment.appointment = appointment
            payment.bill = bill
            payment.amount_paid = bill.amount
            payment.customer = request.user
            payment.save()
            payment.status = 1
            payment.save()
            messages.success(request, 'Payment has been successfully processed.')
            return redirect('pay_opt')
        else:
            form = PaymentForm()
    return render(request,'USER_TEMPLATE/payment.html',{'form':form,'bill':bill})
@login_required
def pay_opt(request):
    return render(request,'USER_TEMPLATE/payment_successful.html')
@login_required
def payed_or_not(request):
    payments = Payment.objects.filter(customer=request.user)
    return render(request, 'USER_TEMPLATE/payment_table.html', {'payments': payments})
@login_required
def pay_success(request,id):
    data = Payment.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect("payed_or_not")
@login_required
def invoice_pdf(request, id):
    bill = Bill.objects.get(id=id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont('Helvetica',18)
    p.drawString(250,750,'Invoice')

    p.rect(50, 50, 500, 750, stroke=1, fill=0)
    p.drawString(100, 700, f"Customer Name: {bill.customer.name}")
    p.drawString(100, 650, f"Worker Name: {bill.worker.name}")
    p.drawString(100, 600, f"Appointment Date: {bill.appointment.schedule.date}")
    p.drawString(100, 550, f"Price: {bill.amount}")

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=invoice_{id}.pdf'
    return response