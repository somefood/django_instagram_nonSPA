# Generated by Django 3.0.8 on 2020-07-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_auto_20200728_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]