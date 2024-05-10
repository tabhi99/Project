from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Image = models.FileField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Entered_By = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name


class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    Specialisation = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Entered_By = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name

class Schedule(models.Model):
    Name = models.CharField(max_length=50)
    Date_Of_Schedule=models.DateField()
    Time_Of_Schedule=models.TimeField()
    Entered_By = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Employee(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    Date_Of_Joining=models.DateField()
    Employee_Status=models.CharField(max_length=50,default="Active")
    

class Deals(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Product_Name=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Entered_By = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    
    
    