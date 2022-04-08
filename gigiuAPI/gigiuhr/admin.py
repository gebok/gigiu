from django.contrib import admin

from gigiuhr.models import Employee, Profile, ResearchCentre

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_code', 'research_centre')
    
    fieldsets = (
        ('Employee information',    {'fields': ['user', 'title', 'gender', 'birth_date', 'marital_status', 'citizenship',
                                                'village', 'district', 'province', 'city_state']}),
        
        ('Employer information',    {'fields': ['research_centre', 'employee_type', 'employee_code', 'hire_date', 
                                                'finish_date']}),
    )


@admin.register(ResearchCentre)
class ResearchCentre(admin.ModelAdmin):
    list_display = ('name', 'district', 'town', 'province')
    
    fieldsets = (
        ('Research Centre',    {'fields': ['name', 'district', 'town', 'province']}),
    )
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user' ,'avatar', 'bio', 'avatar_size')

    fieldsets = (
        ('Bio-data', {'fields': ['user', 'avatar', 'bio']}),
    )
