# Generated by Django 5.0.1 on 2024-01-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_rename_usr_name_userinfo_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
