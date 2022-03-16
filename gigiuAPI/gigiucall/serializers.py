from rest_framework import serializers
from gigiucall.models import CallRegister


class CallRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRegister
        fields = ['id', 'created', 'modified' ,'time', 'call_type', 'receptionist', 'call_requested_by', 'call_to_name',
                  'call_to_org', 'destination', 'phone_number', 'comments', 'created_by', 'modified_by']
        
