from django.db import models

from authentication.models import User
from gigiuhr.models import Employee, ResearchCentre

# Create your models here.


class CallType(models.Model):
    call_type = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.call_type}'
    


class CallRegister(models.Model):
    call_operator = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)
    call_requested_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    call_type = models.ForeignKey(CallType, on_delete=models.CASCADE, default=None, null=True)
    research_centre = models.ForeignKey(
        ResearchCentre, on_delete=models.CASCADE, default=None, null=True)

    phone_number = models.CharField(max_length=15)
    call_made_to = models.CharField(max_length=50)
    destination_org = models.CharField(max_length=100)
    town_province = models.CharField(max_length=100)
    comments = models.TextField(max_length=200)
    date_called = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.call_requested_by.employee_code} - {self.call_operator.first_name}  {self.call_operator.last_name}'


    def call_request_by(self):
        return f'{self.call_operator.first_name} {self.call_operator.last_name}'
    