# Generated by Django 3.1 on 2022-08-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email'),
        ),
    ]
