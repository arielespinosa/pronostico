# Generated by Django 2.2.5 on 2020-07-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0007_auto_20200624_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusercontact',
            name='contact_type',
            field=models.CharField(choices=[('EMAIL', 'Correo electrónico'), ('PHONE', 'Teléfono'), ('CELLPHONE', 'Celular')], max_length=20, null=True),
        ),
    ]
