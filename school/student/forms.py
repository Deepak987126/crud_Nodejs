from django import forms
from . models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Full Name', 'class':'form-control my-2'}))

    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter City', 'class':'form-control my-2'}))

    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Email', 'class':'form-control my-2'}))

    contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number', 'class':'form-control my-2'}))
    class Meta:
        model=Student
        fields =['name','city','email','contact','image'] 