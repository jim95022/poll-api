# Generated by Django 2.2.10 on 2020-11-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_auto_20201115_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]