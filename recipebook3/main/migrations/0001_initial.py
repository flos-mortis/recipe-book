# Generated by Django 3.2.4 on 2021-06-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(default=None, upload_to='image/')),
                ('time', models.PositiveSmallIntegerField()),
                ('complexity', models.TextField()),
                ('portions', models.PositiveSmallIntegerField()),
                ('text', models.TextField()),
                ('video', models.FileField(default=None, upload_to='video/')),
                ('ingredients', models.ManyToManyField(to='main.Ingredients')),
            ],
        ),
    ]
