from django.contrib.auth.forms import UserCreationForm
from service.models import Login, Feedback, WorkerCategory, Schedule, Appointment
from django import forms

class Dateinput(forms.DateInput):
    input_type = 'date'

class Timeinput(forms.TimeInput):
    input_type = 'time'
class CustomerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ("email","name","address","mobile","profilepicture",'username','password1','password2')

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