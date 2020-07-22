# Generated by Django 2.2.5 on 2020-06-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_forecast_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phenomena',
            name='type_of_phenomena',
            field=models.CharField(blank=True, choices=[('DT', 'Depresión Tropical'), ('CT', 'Ciclón Tropical'), ('TT', 'Tormenta Tropical')], max_length=255, null=True),
        ),
    ]