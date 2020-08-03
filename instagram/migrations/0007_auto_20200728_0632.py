# Generated by Django 3.0.8 on 2020-07-28 06:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20200721_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]