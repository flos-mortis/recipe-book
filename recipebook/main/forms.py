from .models import Recipes
from django.forms import ModelForm, TextInput, Textarea


class RecipeForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "text", "photo", "time", "complexity", "ingredients", "video"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст'
            }),

        }
