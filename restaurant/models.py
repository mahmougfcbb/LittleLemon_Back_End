from django.db import models


class Booking(models.Model):
    NUMBER = models.IntegerField()
    NAME = models.CharField(max_length=255)
    TYPE = models.CharField(max_length=255)
  

class Menu(models.Model):
    NUMBER = models.IntegerField()
    NAME = models.CharField(max_length=255)
    TYPE = models.CharField(max_length=255)
    
    #add the following method in Menu class
def __str__(self):
 return f'{self.title} : {str(self.price)}'





