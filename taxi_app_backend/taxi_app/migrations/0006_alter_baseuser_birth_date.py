# Generated by Django 3.2.5 on 2021-09-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0005_alter_baseuser_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
