from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class donor(models.Model):
    National_ID = models.CharField(
    max_length=14,
    validators=[
        MinLengthValidator(14, message='National ID must be at least 14 characters long.'),
    ]
    )
    Name = models.CharField(max_length=50)
    City=models.CharField(max_length=20)
    Email = models.EmailField(max_length=254)

class BloodStock(models.Model):
        Blood_group=models.CharField(max_length=2)
        Bloodbankcity=models.CharField(max_length=20)
        Blood_expiration_date = models.DateTimeField()
        
class HospitalRequest(models.Model):
    hospital_name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=2, choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB')])
    city = models.CharField(max_length=100)
    patient_status = models.CharField(max_length=20, choices=[('Immediate', 'Immediate'), ('Urgent', 'Urgent'), ('Normal', 'Normal')])
        