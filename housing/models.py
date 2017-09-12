from django.db import models
from django.utils import timezone

# Create your models here.

class Room(models.Model):
    """Class Modelling Rooms """
    number = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Room No: " + str(self.number)


class Status(models.Model):
    room = models.OneToOneField(Room)
    status = models.CharField(max_length=15, choices=(
        ('available', 'Available'),
        ('booked', 'Booked'),
        #('reserved', 'Reserved'),
    ))

    def __str__(self):
        if self.status == 'available':
            status = 'Available'
        else:
            status = 'Booked'
        return "Room No: " + str(self.room.number)  + ' Current Status : ' + str(status)

