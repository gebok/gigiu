from django.contrib import admin

from gigiucall.models import CallRegister, CallType

# Register your models here.


@admin.register(CallRegister)
class CallRegisterAdmin(admin.ModelAdmin):
    list_display = ('call_requested_by', 'call_made_to',  'call_operator', 'phone_number',
                    'destination_org', 'date_called', 'comments')
    
    fieldsets = (
        ('Call Origin',         {'fields': ['research_centre', 'call_type', 'call_requested_by', 'call_operator']}),
        ('Call Destination',    {'fields': ['call_made_to', 'phone_number', 'destination_org', 'town_province', 
                                            'comments']}),
    )


@admin.register(CallType)
class CallTypeAdmin(admin.ModelAdmin):
    list_display = ('call_type',)
