from django import forms
from .models import BlogPost
from django.forms import TextInput,Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostBlogForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=('Title','Blog_Content')

        widgets={
            'Title':TextInput(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':'Blog Title'
            }),
            'Blog_Content':Textarea(attrs={
                'class':'form-control',
                'style':'max-width:400px'
            })
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2','check']
    email=forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
    )
    first_name=forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LastName'}),
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placehol.der': 'Confirm Password'})
    )
    check=forms.BooleanField(required=True)







