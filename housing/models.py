from django.db import models

# Create your models here.

class Room(models.Model):
    """Class Modelling Rooms """
    number = models.IntegerField()

    def __str__(self):
        return "Room No: " + str(self.number)


class Status(models.Model):
    room = models.OneToOneField(Room)
    status = models.CharField(max_length=15, choices=(
        ('available', 'Available'),
        ('booked', 'Booked'),
    ))

    def __str__(self):
        if self.status == 'available':
            status = 'Available'
        else:
            status = 'Booked'
        return "Room No: " + str(self.room.number)  + ' Current Status : ' + str(status)

