from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipeForm


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

    return render(request, 'add.html', {'error': error})


# page show recipe
def recipe(request):
    # method for get need recipe
    form = RecipeForm()
    return redirect(request, 'main/recipe.html', {'recipe': form})


def autor(request):
    return render(request, 'autor.html')


def register(request):
    return render(request, 'register.html')


def search(request):
    return render(request, 'search.html')


def profile(request):
    return render(request, 'profile.html')
