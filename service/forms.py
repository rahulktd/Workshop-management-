from django.contrib.auth.forms import UserCreationForm
# from django.forms import forms
from service.models import Login, Feedback, WorkerCategory
from django import forms
#
#
class CustomerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ("email","name","address","mobile","profilepicture",'username','password1','password2')


class WorkerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ("email","name","address","mobile","profilepicture","Work_Category",'username','password1','password2')
        widgets = {'profilepicture':forms.ClearableFileInput(attrs={'style': ' padding-bottom: 10px;padding-top:8px; border-radius: 5px;'})}
#
#
# class LoginRegister(UserCreationForm):
#     username = forms.CharField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
#     class Meta:
#         model = Login
#         fields = ('username', 'password1', 'password2')
#
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)
#
class SkillForm(forms.ModelForm):
    class Meta:
        model = WorkerCategory
        fields = ('Title',)