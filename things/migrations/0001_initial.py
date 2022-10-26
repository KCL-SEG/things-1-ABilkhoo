# Generated by Django 4.1.2 on 2022-10-26 08:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Min quantity is 0'), django.core.validators.MaxValueValidator(100, 'Max quantity is 100')])),
            ],
        ),
    ]