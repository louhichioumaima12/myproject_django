from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Specialty(models.Model):
    name = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name ='Specialty'
        verbose_name_plural ="Specialtys"
        def __str__(self):
              return self.name

class User(AbstractUser):
    pass

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)
    specialties = models.ManyToManyField(Specialty,related_name='doctors')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #specialty =models.ManyToManyField("AccountApp.Speciality")
    specialties = models.ManyToManyField(Specialty,related_name='doctors')
    number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Le numéro doit contenir exactement 8 chiffres."
     
)
    class Meta:
                verbose_name ='Doctor'
                verbose_name_plural ="Doctors"

    def validate_birth_date(v):
        if v>=timezone.localdate():
            raise ValidationError("la date de naissance ne peut pas etre dans le future .")

        
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
                verbose_name ='Patient'
                verbose_name_plural ="Patients"