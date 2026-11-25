from django.contrib import admin
from .models import Appointment

#@admin.register(Appointment)
@admin.register(description="Make them confirmed")
def confirmed_appointment(model,req,queryset):
    queryset.update(status='CONFRIRMED')
    
class appointmentAdminPers(admin.ModelAdmin):
    actions=[confirmed_appointment]
    list_display=("reason","status","duration_minutes","appointment_date")
    list_filter=("status","appointment_date")
    #list_editable=("status")
    search_field=("reason","status")
    ordering=("-appointment_date",)
    fieldsets=(
        ('Description ',{
            'fields':("reason","status","prescription")
        }),
        ("Date + Duration",{
           'fields':("appointment_date","duration_minutes")
        }),
        ("Patients/Doctors",{
            'fields':("doctor","patient")
                }),
         ("Patients/Doctors",{
            'fields':("doctor","patient")
         }),  
   ("Planification",{
               'fields':("created_at","updated_at")
            })

    )
    readonly_fields=("created_at","updated_at")
