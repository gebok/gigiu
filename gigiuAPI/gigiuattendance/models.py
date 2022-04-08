from django.db import models

from authentication.models import User
from gigiuhr.models import Employee, ResearchCentre

# Create your models here.

class Attendance(models.Model):
    dept = models.ForeignKey(ResearchCentre, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    enrol_id = models.CharField(max_length=4)
    date = models.DateField(null=True, blank=True)
    clock_in = models.TimeField(null=True, blank=True)
    clock_out = models.TimeField(null=True, blank=True)
    comment = models.TextField()
    
    def __str__(self):
        return f'{self.enrol_id}'