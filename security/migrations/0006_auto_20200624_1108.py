# Generated by Django 2.2.5 on 2020-06-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0005_auto_20200624_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusercontact',
            name='contact_type',
            field=models.CharField(choices=[('EMAIL', 'Correo electrónico'), ('CELLPHONE', 'Celular'), ('PHONE', 'Teléfono')], max_length=20, null=True),
        ),
    ]
