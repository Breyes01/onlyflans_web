# Generated by Django 5.0.7 on 2024-07-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flan', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.FloatField(default=4.99),
        ),
    ]
