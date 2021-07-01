from django.db import models


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient


class Recipes(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='image/', default=None)
    ingredients = models.ManyToManyField(Ingredients)
    time = models.PositiveSmallIntegerField()
    complexity = models.TextField()
    portions = models.PositiveSmallIntegerField()
    text = models.TextField()
    video = models.FileField(upload_to='video/', default=None)

    def __str__(self):
        return self.name
