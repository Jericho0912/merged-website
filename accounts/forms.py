from django.forms import ModelForm
from .models import Product ,  userinfo , clientinfo
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addlist(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description']


        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control w-75'}),
            'price' : forms.TextInput(attrs={'class':'form-control w-75'}),
            'description' : forms.TextInput(attrs={'class':'form-control w-75'}),
        }
        
class deletelist(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


        
class updateinfo(ModelForm):
    class Meta:
        model = userinfo
        fields = ['fname','lname','phone','email']

        labels = {
            'fname':'Enter Your Firstname',
            'lname':'Enter Your Lastname',
            'phone':'Enter Your PhoneNumber',
            'email':'Enter Your Email',
        }

        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control w-75'}),
            'lname':forms.TextInput(attrs={'class':'form-control w-75'}),
            'phone':forms.TextInput(attrs={'class':'form-control w-75'}),
            'email':forms.EmailInput(attrs={'class':'form-control w-75'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class Createclient(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username','email','password1','password2']
