# Generated by Django 5.0.1 on 2024-03-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_map_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
