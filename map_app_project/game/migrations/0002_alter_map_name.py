# Generated by Django 5.0.1 on 2024-03-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
