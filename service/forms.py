from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from service.models import Login, Feedback, WorkerCategory, Schedule, Appointment, Bill, Payment
from django import forms

class Dateinput(forms.DateInput):
    input_type = 'date'

class Timeinput(forms.TimeInput):
    input_type = 'time'
# class CustomerForm(UserCreationForm):
#     class Meta:
#         model = Login
#         fields = ("email","name","address","mobile","profilepicture",'username','password1','password2')
class CustomerForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    mobile = forms.CharField(max_length=10, help_text='Required. Enter a valid 10 digit mobile number.')

    class Meta:
        model = Login
        fields = ("email","name","address","mobile","profilepicture",'username','password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Login.objects.filter(email=email).exists():
            raise ValidationError(_('This email address is already in use.'))
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit() or len(mobile) != 10:
            raise ValidationError(_('Please enter a valid 10 digit mobile number.'))
        return mobile

class WorkerForm(UserCreationForm):
    birth_date = forms.DateField(widget=Dateinput)
    class Meta:
        model = Login
        fields = ("email","name",'birth_date',"address","mobile","profilepicture","Work_Category",'username','password1','password2')
        widgets = {'profilepicture':forms.ClearableFileInput(attrs={'style': ' padding-bottom: 10px;padding-top:8px; border-radius: 5px;'})}

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)
#
class SkillForm(forms.ModelForm):
    class Meta:
        model = WorkerCategory
        fields = ('Title',)


class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=Dateinput)
    start_time = forms.TimeField(widget=Timeinput)
    end_time = forms.TimeField(widget=Timeinput)
    class Meta:
        model = Schedule
        fields = ('date', 'start_time', 'end_time')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('worker','schedule','status')


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('customer','amount')

class BillApprovalForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ()


class PaymentForm(forms.ModelForm):
    exp= forms.DateField(widget=Dateinput)
    class Meta:
        model = Payment
        fields = ('card_number', 'cvv', 'exp')