from django.db import models
from authentication.models import User

# Create your models here.


class ResearchCentre(models.Model):
    name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee',)
    research_centre = models.ForeignKey(ResearchCentre, on_delete=models.CASCADE)

    employee_code = models.CharField(max_length=5)
    employee_type = models.CharField(max_length=10)
    title = models.CharField(max_length=5)
    gender = models.CharField(max_length=6)
    marital_status = models.CharField(max_length=10)
    citizenship = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city_state = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.employee_code} - {self.user.first_name} {self.user.last_name}'

    def fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def researchcentre(self):
        return f'{self.research_centre.rc_name}'

# Extending User model using a one-to-one relationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(null=True)
    avatar_size = models.IntegerField(null=True)
    modified_by = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'