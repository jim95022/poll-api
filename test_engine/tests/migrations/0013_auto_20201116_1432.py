# Generated by Django 2.2.10 on 2020-11-16 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_auto_20201116_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='user_id',
            new_name='user',
        ),
    ]