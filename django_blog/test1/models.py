from django.db import models
import datetime

class Company(models.Model):
    name=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True)
    date_created=models.DateTimeField(default=datetime.date.today,blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=30)
    creator=models.CharField(max_length=50)
    date_created=models.DateField()
    def __str__(self):
        return self.creator



class Customer(models.Model):
    name=models.CharField(max_length=200)

class Vehicle(models.Model):
    name=models.CharField(max_length=200)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,related_query_name='CustomerVehicle')
class Bank(models.Model):
    bank_name=models.CharField(max_length=250)
class Location(models.Model):
    bank_location=models.CharField(max_length=255)
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE,related_name='LocationBank')

class Programmer(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    company= models.ForeignKey(Company,on_delete=models.CASCADE)
    languages=models.ManyToManyField(Language)

# Create your models here.
