from datetime import timedelta
from django.db import models
from security.models import AppUser
from django.utils import timezone
import pytz 

# Phenomena
class Phenomena(models.Model):
    TYPE_OF_PHENOMENA = {
        ('DT', 'Depresión Tropical'),
        ('TT', 'Tormenta Tropical'),
        ('CT', 'Ciclón Tropical'),
    }
    name = models.CharField(max_length=255, blank=True, null=True)
    type_of_phenomena = models.CharField(max_length=255, choices=TYPE_OF_PHENOMENA, blank=True, null=True)

# Document
class Document(models.Model):    
    # When the user create de forecast
    creation_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    # The datetime than document make reference
    emision_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    emision_date_utc = models.DateTimeField(default=timezone.now, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    leyend = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    main_author = models.ForeignKey(AppUser, related_name='main_author', on_delete=models.CASCADE, blank=True, null=True)
    authors = models.ManyToManyField(AppUser, related_name='secondary_author', blank=True)

    class Meta:
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.name

    def emision_date_in_utc(self):
        #TZ_GMT0 = pytz.timezone('Etc/GMT-0')
        return self.emision_date.astimezone(pytz.timezone('America/Bogota'))

# DP10
class DP10(Document):
    code = models.CharField(default='FECU42 MUHV', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Discusión de Plazo Medio'

    def __str__(self):
        return 'Discusión de Plazo Medio'
    
    def typeof(self):
        return 'DP10'
    
    def vaild_timespace(self):
        return {
            "initial": self.emision_date + timedelta(days=2), 
            "end": self.emision_date + timedelta(days=11)
            }

# PTTN
class PTTN(Document):
    code = models.CharField(default='FECU42 MUHV', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Pronóstico del Tiempo para la Tarde y la Noche'
    
    def typeof(self):
        return 'PTTN'

# EGT00
class EGT(Document):
    code = models.CharField(default='AXCU40 MUHV', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Estado General del Tiempo'

    def __str__(self):
        return 'Estado General del Tiempo'
    
    def typeof(self):
        return 'EGT'
    
    def vaild_timespace(self):
        return None

# ACT
class ACT(Document):
    phenomena = models.ForeignKey(Phenomena, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Avisos de Ciclones Tropicales'

    def __str__(self):
        return 'Aviso de Ciclón Tropical No. ' + str(self.pk)
    
    def typeof(self):
        return 'ACT'

# AE
class AE(Document):
    no = models.IntegerField(blank=True, null=True)
    code = models.CharField(default='FECU42 MUHV 121530', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Avisos Especiales'

    def __str__(self):
        return 'Aviso Especial No. ' + str(self.no)
    
    def typeof(self):
        return 'AE'

# NI
class NI(Document):
    class Meta:    
        verbose_name_plural = 'Notas Informativas'

    def __str__(self):
        return 'Nota Informativa No.' + str(self.pk)
    
    def typeof(self):
        return 'Nota Informativa'

# PT5
class PT5(Document):    
    sinopsis = models.CharField(max_length=250, blank=True, null=True)
    day1 = models.TextField(blank=True, null=True)
    day2 = models.TextField(blank=True, null=True)
    day3 = models.TextField(blank=True, null=True)
    day4 = models.TextField(blank=True, null=True)
    day5 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'PT5'

    def __str__(self):
        return 'PT5 No. ' + str(self.pk)
    
    def typeof(self):
        return 'PT5'

# PTM
class PTM(Document):
    interest_aditional_info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'PTM'

    def __str__(self):
        return 'PTM No. ' + str(self.pk)
    
    def typeof(self):
        return 'PTM'

# PTHOY
class PTHOY(Document):
    interest_aditional_info = models.TextField(blank=True, null=True)
  
    class Meta:
        verbose_name_plural = 'PTHOY'

    def __str__(self):
        return 'PTHOY ' + str(self.pk)
    
    def typeof(self):
        return 'PTHOY'

# PTRD
class PTRD(Document):
    class Meta:
        verbose_name_plural = 'PTRD'

    def __str__(self):
        return 'PTRD No. ' + str(self.pk)
    
    def typeof(self):
        return 'PTRD'

# PTT
class PTT(Document):
    class Meta:
        verbose_name_plural = 'PTT'

    def __str__(self):
        return 'PTT No. ' + str(self.pk)
    
    def typeof(self):
        return 'PTT'






