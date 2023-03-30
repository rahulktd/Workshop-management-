from django.contrib import messages
from django.shortcuts import redirect, render

from service.forms import FeedbackForm


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
            return redirect('feedback_view')
    else:
        feedback_form = FeedbackForm
    return render(request,'USER_TEMPLATE/customer_feedback.html',{'feedback_form':feedback_form})

def feedback_view(request):
    return render(request,'USER_TEMPLATE/USER_DASH.html')
