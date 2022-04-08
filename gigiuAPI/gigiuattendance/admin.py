from django.contrib import admin

from gigiuattendance.models import Attendance

# Register your models here.


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('dept', 'user_id', 'name', 'enrol_id', 'date', 'clock_in', 'clock_out', 'comment')
    
    fieldsets = (
        ('Attendance information',    {'fields': ['dept', 'user_id', 'name', 'enrol_id', 'date', 'clock_in', 
                                                  'clock_out', 'comment']}),
    )
