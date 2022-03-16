from django.db import models

# Create your models here.


class CallRegister(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    time = models.TimeField(auto_now_add=True)

    OFFICIAL = 'Official'
    PERSONAL = 'Personal'
    TYPE = [ (OFFICIAL, 'Official'), (PERSONAL, 'Personal'), ]
    
    call_type = models.CharField(
        max_length=10, choices=TYPE, default=OFFICIAL)

    AA = 'Anna AGIO'
    MD = 'Madeleine DICKSON'
    BS = 'Bridgit SAMOR'
    GW = 'Gloria WINGAWE'
    CALL_MADE_BY = [ (AA, 'Anna AGIO'), (BS, 'Bridgit SAMOR'), (GW, 'Gloria WINGAWE'), (MD, 'Madeleine DICKSON'), ]
                    
    receptionist = models.CharField(
        max_length=20, choices=CALL_MADE_BY, default=AA)
    
    call_requested_by = models.CharField(max_length=20)
    call_to_name = models.CharField(max_length=50)
    call_to_org = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    comments = models.TextField(max_length=200)
    
    created_by = models.CharField(
        max_length=30, choices=CALL_MADE_BY, default=AA)
    modified_by = models.CharField(
        max_length=30, choices=CALL_MADE_BY, default=AA)

    class Meta:
        ordering = ['created']
        