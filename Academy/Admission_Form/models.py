from django.db import models

# Create your models here.
from django.db import models

class Admission(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    CLASS_CHOICES = [
        ('9th', '9th Class'),
        ('10th', '10th Class'),
        ('1st Year Medical', '1st Year Medical'),
        ('1st Year Non-Medical', '1st Year Non-Medical'),
        ('1st Year ICS', '1st Year ICS'),
    ]
    
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    cnic = models.CharField(max_length=15)
    domicile = models.CharField(max_length=100)
    student_class = models.CharField(max_length=30, choices=CLASS_CHOICES)
    photo = models.ImageField(upload_to='student_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    fees = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
    