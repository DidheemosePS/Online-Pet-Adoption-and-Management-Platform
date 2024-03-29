from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Take_Care.models import Post
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User

# Signup / Create a user form


class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=75, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login form


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# # Form to create an event


class CreatePostsForm(forms.ModelForm):
    owner_name = forms.CharField(
        label="Owner Name", max_length="100", required=True)
    pet_name = forms.CharField(
        label="Pet Name", max_length=100, required=True)
    pet_category = forms.CharField(
        label="Category", max_length=100, required=True)
    pet_age = forms.IntegerField(
        label="Age", required=True)
    pet_description = forms.CharField(
        label="Description",
        required=True,
        widget=forms.Textarea(attrs={'rows': 5})
    )
    pet_address = forms.CharField(
        label="Address",
        required=True,
        widget=forms.Textarea(attrs={'rows': 5})
    )
    pet_image = forms.FileField(label="Image", required=True, widget=forms.FileInput(
        attrs={'type': "file", 'accept': "image/png, image/jpeg"}))

    class Meta:
        model = Post
        fields = ['owner_name', 'pet_name', 'pet_category',
                  'pet_age', 'pet_description', 'pet_address', 'pet_image']
