# Generated by Django 4.2.3 on 2023-11-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]