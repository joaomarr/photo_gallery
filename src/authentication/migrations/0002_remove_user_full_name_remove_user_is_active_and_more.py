# Generated by Django 4.1 on 2022-08-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='user',
            name='is_friend',
            field=models.BooleanField(default=True, verbose_name='Friend'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_married',
            field=models.BooleanField(default=False, verbose_name='Married'),
        ),
    ]
