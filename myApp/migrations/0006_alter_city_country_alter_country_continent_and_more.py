# Generated by Django 4.2 on 2023-04-24 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_alter_continent_continent_img_alter_country_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='myApp.country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='myApp.continent'),
        ),
        migrations.AlterField(
            model_name='dateweather',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dateweather', to='myApp.city'),
        ),
    ]