# Generated by Django 4.0.3 on 2022-04-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_registrationmodel_city_registrationmodel_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='course',
            field=models.CharField(max_length=8),
        ),
    ]