from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipeForm
from .models import Recipes
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm
from django.views.generic import CreateView

# main page with all recipes
def main(request):
    return render(request, 'main.html')


# page add recipe
def add(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'неверно введены данные'
    form = RecipeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add.html', context)


# page show recipe
def recipe(request):
    return render(request, 'recipe.html')


class RegisterUser(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_msg = 'Пользователь успешно создан.'



class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url


def search(request):
    return render(request, 'search.html')


def profile(request):
    return render(request, 'profile.html')
