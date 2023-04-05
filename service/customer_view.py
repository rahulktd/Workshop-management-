from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404

from service.forms import FeedbackForm
from service.models import Customer, Feedback


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

# def feedback_view(request):
#     return render(request,'USER_TEMPLATE/customer_feedback_view.html')
def customer_feedback_view(request):
    u = request.user
    feedback=Feedback.objects.filter(user=u)
    return render(request,'USER_TEMPLATE/customer_feedback_view.html',{'feedback':feedback})

# def customer_detail(request, customer_id):
#     customer = get_object_or_404(Customer, id=customer_id)
#     return render(request, 'USER_TEMPLATE/USER_DASH.html', {'customer': customer})


def reply_view(request):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        reply_v = request.POST.get('reply')
        feedback.reply = reply_v
        feedback.save()
        return redirect('reply_view', id=id)
    else:
        form = FeedbackForm()
    return render(request, 'USER_TEMPLATE/customer_feedback_view.html', {'feedback': feedback,})

