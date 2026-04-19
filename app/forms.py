from django import forms

class UserLogin(forms.Form):
    name=forms.CharField(label="Name",max_length=30)
    password=forms.CharField(label="Password",max_length=20)
