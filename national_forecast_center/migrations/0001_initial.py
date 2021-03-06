# Generated by Django 2.2.5 on 2020-06-24 14:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('emision_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('emision_date_utc', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('leyend', models.CharField(blank=True, max_length=250, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, null=True, related_name='secondary_author', to='security.AppUser')),
                ('main_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_author', to='security.AppUser')),
            ],
            options={
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Phenomena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_phenomena', models.CharField(blank=True, choices=[('TT', 'Tormenta Tropical'), ('DT', 'Depresión Tropical'), ('CT', 'Ciclón Tropical')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AE',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('no', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, default='FECU42 MUHV 121530', max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Avisos Especiales',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='DP10',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('code', models.CharField(blank=True, default='FECU42 MUHV', max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Discusión de Plazo Medio',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='EGT',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('code', models.CharField(blank=True, default='AXCU40 MUHV', max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Estado General del Tiempo',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='NI',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
            ],
            options={
                'verbose_name_plural': 'Notas Informativas',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='PT5',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('sinopsis', models.CharField(blank=True, max_length=250, null=True)),
                ('day1', models.TextField(blank=True, null=True)),
                ('day2', models.TextField(blank=True, null=True)),
                ('day3', models.TextField(blank=True, null=True)),
                ('day4', models.TextField(blank=True, null=True)),
                ('day5', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'PT5',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='PTHOY',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('interest_aditional_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'PTHOY',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='PTM',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('interest_aditional_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'PTM',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='PTRD',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
            ],
            options={
                'verbose_name_plural': 'PTRD',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='PTT',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
            ],
            options={
                'verbose_name_plural': 'PTT',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='PTTN',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
            ],
            options={
                'verbose_name_plural': 'PTTN',
            },
            bases=('national_forecast_center.document',),
        ),
        migrations.CreateModel(
            name='ACT',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='national_forecast_center.Document')),
                ('phenomena', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='national_forecast_center.Phenomena')),
            ],
            options={
                'verbose_name_plural': 'Avisos de Ciclones Tropicales',
            },
            bases=('national_forecast_center.document',),
        ),
    ]
