# Generated by Django 3.2.3 on 2021-06-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210606_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='css',
            field=models.BooleanField(default=False, verbose_name='CSS'),
        ),
        migrations.AddField(
            model_name='skills',
            name='html',
            field=models.BooleanField(default=False, verbose_name='HTML'),
        ),
        migrations.AddField(
            model_name='skills',
            name='js',
            field=models.BooleanField(default=False, verbose_name='JS'),
        ),
    ]
