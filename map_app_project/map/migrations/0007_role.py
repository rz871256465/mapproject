# Generated by Django 4.2 on 2024-02-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_userinfo_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(default='普通用户', max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
                ('user_to_role', models.ManyToManyField(related_name='roles', to='map.userinfo')),
            ],
        ),
    ]
