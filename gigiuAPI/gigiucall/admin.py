from django.contrib import admin
from .models import CallRegister

# Register your models here.


@admin.register(CallRegister)
class CallRegisterAdmin(admin.ModelAdmin):
    list_display = ('call_requested_by', 'call_to_name', 'call_to_org', 'phone_number', 'created')
