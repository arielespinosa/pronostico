from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ForecastCenter(models.Model):
    name = models.CharField(max_length = 30, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Centros'

    def __str__(self):
        return self.name

#--------------------------------------------------------------------------------------
class AppUser(models.Model):
    SCIENTIFIC_CATEGORY = [
        ('Dr.', 'Doctor'),
        ('Dra.', 'Doctora'),
        ('Msc.', 'Master en Ciencias'),
        ('Lic.', 'Licenciado'),
        ('Ing.', 'Ingeniero'),
        ('Téc.', 'Técnico'),
    ]

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    avatar = models.ImageField(upload_to='user_avatar', null=True)   
    lastname1 = models.CharField(max_length = 30)
    lastname2 = models.CharField(max_length = 30)
    ocupation = models.CharField(max_length = 30)
    category = models.CharField(max_length=50, choices=SCIENTIFIC_CATEGORY, null=True)
    forecast_center = models.ForeignKey(ForecastCenter, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def full_name(self):
        return self.name + ' ' + self.lastname1 + ' ' + self.lastname2

    def sign_name(self):
        return self.category + ' ' + self.full_name()

    def get_absolute_url(self):
        return reverse("user_profile_view", kwargs={"id":self.id})
   

#--------------------------------------------------------------------------------------
class AppUserContact(models.Model):
    CONTACT_CHOICES = {
        ('PHONE', 'Teléfono'),
        ('CELLPHONE', 'Celular'),
        ('EMAIL', 'Correo electrónico'),
    }
    appuser = models.ForeignKey(AppUser, null=True, blank=True, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=20, null=True, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=20, null=True)
