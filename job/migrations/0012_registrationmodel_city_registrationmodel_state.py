# Generated by Django 4.0.3 on 2022-04-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_remove_registrationmodel_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
    ]