# Generated by Django 3.2.5 on 2021-09-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0004_baseuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]