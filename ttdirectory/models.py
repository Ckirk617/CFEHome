from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class PolicyArea(models.Model):
    topic = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.topic
    
class Staff(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=50)
    mission_statement = models.TextField()
    year_founded = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=50)
    city = models.ForeignKey(City,on_delete=models.PROTECT)
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    policy_areas = models.ManyToManyField(PolicyArea)   
    staff = models.ManyToManyField(Staff)
    
    def __str__(self):
        return self.name
    # Programs
    





    
    
"""

Things to include:
    staff/experts
    about/mission statement
    policy areas/specializations
    university affiliation ??
    programs?? like fellowship programs??
    

"""