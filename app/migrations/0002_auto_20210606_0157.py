# Generated by Django 3.2.3 on 2021-06-05 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Персоны', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Навыки', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Задачи', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='skills',
            name='text',
            field=models.CharField(max_length=254, null=True, verbose_name='Навык'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='text',
            field=models.TextField(null=True, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task',
            field=models.BooleanField(),
        ),
    ]