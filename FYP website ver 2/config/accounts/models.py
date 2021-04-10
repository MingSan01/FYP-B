# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    
    def __str__(self):
        return self.email

    class Meta:"accounts_customuser"
        
class UserReport (models.Model):
    
    scan_data = models.CharField (max_length=100)
    scan_website = models.TextField()
    vulnerabilities = models.TextField()
    solutions = models.TextField()
    date = models.DateTimeField()
    scan_type = models.TextField()
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table:"accounts_userreport"


class UserPortReport (models.Model):

    host_data = models.CharField (max_length=100)
    state = models.TextField()
    protocol = models.TextField()
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        
