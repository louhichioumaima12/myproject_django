from django.contrib import admin
from .models import *
from .models import Appointment



admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Specialty)
class AppointmentStackedInline(admin.StackedInline):
       model=Appointment
       extra=1
class DoctorPersoClass(admin.ModelAdmin):
       inlines=[AppointmentStackedInline,]
       admin.site.register(Doctor,DoctorPersoClass)
       admin.site.register(Specialty)
       

# Register your models here.
