from rest_framework import serializers
from gigiucall.models import CallRegister


class CallRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallRegister
        fields = ['id', 'call_operator', 'call_requested_by','call_type', 'research_centre', 
                  'phone_number', 'call_made_to', 'destination_org', 'town_province', 
                  'comments', 'date_called', 'updated_at', 'modified_by']
        