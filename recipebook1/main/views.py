from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipeForm


# main page with all recipes
def main(request):
    recipe = Recipes.objects.order_by('-id')
    return render(request, 'main.html', {'recipes': recipe})


# page add recipe
def add(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'неверно введены данные'

    return render(request, 'add.html', {'error': error})


# page show recipe
def recipe(request):
    # method for get need recipe
    form = RecipeForm()
    return redirect(request, 'main/recipe.html', {'recipe': form})


def autor(request):
    return render(request, 'main/templates/autor.html')


def register(request):
    return render(request, 'main/templates/register.html')


def search(request):
    return render(request, 'main/templates/search.html')


def profile(request):
    return render(request, 'main/templates/profile.html')
