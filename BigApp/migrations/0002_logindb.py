# Generated by Django 5.0.4 on 2024-05-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='logindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
