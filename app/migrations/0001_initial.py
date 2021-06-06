# Generated by Django 3.2.3 on 2021-06-05 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.BooleanField(verbose_name='Навык')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.BooleanField(verbose_name='Задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=200, verbose_name='Отчество')),
                ('number', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.skills', verbose_name='Навыки')),
                ('tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tasks', verbose_name='Задачи')),
            ],
        ),
    ]