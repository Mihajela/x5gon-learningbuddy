# Generated by Django 3.0.3 on 2020-02-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200219_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='proffesional',
            field=models.BooleanField(default=False),
        ),
    ]