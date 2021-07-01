from .models import Recipes
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RecipeForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "text", "photo", "time", "complexity", "portions", "ingredients", "video"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "complexity": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сложность приготовления'
            }),
            "ingredients": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ингредиенты'
            }),

        }

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"text",
    }), label = "Логин")

    password = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"password",
    }), label = "Пароль")

    email = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"email",
    }), label = "Почта")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
