# Generated by Django 4.0.1 on 2022-01-28 00:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('about', models.TextField(max_length=300)),
                ('serves', models.PositiveIntegerField()),
                ('ingredients_produce', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('ingredients_drinks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('ingredients_spirit', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('ingredients_other', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('recipe', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=3000), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_by', to='cocktails.cocktail')),
            ],
        ),
    ]
