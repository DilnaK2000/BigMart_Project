# Generated by Django 5.0.4 on 2024-05-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigApp', '0005_cartdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdb',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
