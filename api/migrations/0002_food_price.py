# Generated by Django 4.1.1 on 2022-10-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
