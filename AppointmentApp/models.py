from django.db import models
from django.conf import settings
from AccountApp.models import Doctor,Patient
from django.core.exceptions import ValidationError 
from django.utils import timezone


class Appointment(models.Model):
   reason =models.TextField()
   prescription =models.FileField(
        blank=True,
        upload_to='prescriptions/'
   )
class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'
status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )

   

duration_minutes = models.PositiveIntegerField(default=30)
appointment_date = models.DateTimeField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
appointment_data = models.DateTimeField();
doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
patient =models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
def clean(self):
     modified_date = self._state.adding or (
        Appointment.objects.filter(
            pk=self.pk,
            appointment_date=self.appointment_date
        ).exists()
    )
     if self.appointment_date <= timezone.now():
          raise ValidationError ("la date du rdv doit etre supperieur a la date d'aujourd'huit ")
class Meta:
    ordering = ["-appointment_date"]

    constraints = [
        models.UniqueConstraint(
            fields=["doctor", "appointment_date"],
            name="unique_doctor_date",
            violation_error_message="Ce docteur possède déjà un rendez-vous à cette date."
        )
    ]

    def __str__(self):
         return f"le rdv est pour la raison{self.reason} "