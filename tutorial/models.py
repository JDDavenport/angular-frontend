# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class prescriber(models.Model):
    DoctorID = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    credentials = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    OpioidPrescriber = models.IntegerField()
    totalprescriptions = models.IntegerField()

    def __str__(self):
        return ' %s %s %s %s %s %s %s %s %s ' % (self.DoctorID, self.fname, self.lname, self.gender, self.state, self.credentials, self.specialty, self.OpioidPrescriber, self.totalprescriptions)
    
class overdoses(models.Model):
    state = models.CharField(max_length=200)
    population = models.CharField(max_length=300)
    deaths = models.CharField(max_length=300)
    abbrev = models.CharField(max_length=300)
    def __str__(self):
        return ' %s %s %s %s ' % (self.state, self.population, self.deaths, self.abbrev)

class docdrugqty(models.Model):
    DoctorID = models.IntegerField()
    drug = models.CharField(max_length=300)
    qty = models.IntegerField()
    def __str__(self):
        return ' %s %s %s ' % (self.DoctorID, self.drug, self.qty)

class dangerscore(models.Model):
    DoctorID = models.IntegerField()
    dangerscore = models.IntegerField()

    def __str__(self):
        return ' %s %s ' % (self.DoctorID, self.dangerscore)



