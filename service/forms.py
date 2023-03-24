from django.contrib.auth.forms import UserCreationForm
# from django.forms import forms
from service.models import Login, Customer, Worker
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ("user",)

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        exclude = ("user",)

class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')