# Generated by Django 4.2 on 2024-02-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_userinfo_user_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
