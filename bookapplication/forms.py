from django import forms
from bookapplication.models import Books
from django.contrib.auth.models import User

class BookModelForms(forms.ModelForm):

     class Meta:
          model=Books
          fields="__all__"

    
     widgets={
               "bname":forms.TextInput(attrs={"class":"form-control"}),
               "prize":forms.NumberInput(attrs={"class":"form-control"}),
               "Date":forms.DateInput(attrs={"class":"form-control"}),
               "author":forms.TextInput(attrs={"class":"form-control"}),
             

          }
    
class RegistrationForm(forms.ModelForm):

     class Meta:
          model=User
          fields=["username","email","password"]


class LoginForm(forms.Form):
     username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
       