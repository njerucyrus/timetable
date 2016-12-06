from django.contrib import admin
from availability.models import Lecturer, LecturerAvailability
# Register your models here.


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['lecturer_code', 'phone_number']

    class Meta:
        model = Lecturer
admin.site.register(Lecturer, LecturerAdmin)


class LecturerAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['lecturer', 'day', 'from_hr', 'to_hr']

    class Meta:
        model = LecturerAvailability
admin.site.register(LecturerAvailability, LecturerAvailabilityAdmin)