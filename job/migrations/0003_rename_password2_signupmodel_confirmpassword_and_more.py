# Generated by Django 4.0.3 on 2022-04-10 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_signupmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupmodel',
            old_name='password2',
            new_name='confirmpassword',
        ),
        migrations.RenameField(
            model_name='signupmodel',
            old_name='password1',
            new_name='password',
        ),
    ]
