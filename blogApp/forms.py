from .models import Category, Blog, UserTable, Login, Signin
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)


class UserTableForm(UserCreationForm):
    class Meta:
        model = UserTable
        fields=('username','password','email', 'phone', 'address')


class BlogForm(UserCreationForm):
    class Meta:
        model = Blog
        fields=('title', 'content','pic' )


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields=('username','password')
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
        

class SigninForm(UserCreationForm):
    class Meta:
        model = Signin
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'address')