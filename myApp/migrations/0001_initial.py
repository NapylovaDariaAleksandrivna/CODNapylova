# Generated by Django 4.1.7 on 2023-04-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('city_name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent_name', models.CharField(max_length=30)),
                ('continent_img', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(max_length=30)),
                ('country_name', models.CharField(max_length=30)),
                ('flag', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DateWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('weather_status', models.CharField(max_length=30)),
                ('status_icon', models.CharField(max_length=30)),
                ('wind_speed', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
        ),
    ]
