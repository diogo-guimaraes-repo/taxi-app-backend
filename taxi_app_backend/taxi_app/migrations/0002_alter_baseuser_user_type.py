# Generated by Django 3.2.5 on 2021-07-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'client'), (2, 'driver'), (3, 'admin')], default=1),
        ),
    ]
