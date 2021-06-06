# Generated by Django 3.2.3 on 2021-06-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210606_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='analytics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='models',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='platform',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='css',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='django',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='html',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='js',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='php',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='python',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='react',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='ux',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='vue',
            field=models.BooleanField(default=False),
        ),
    ]