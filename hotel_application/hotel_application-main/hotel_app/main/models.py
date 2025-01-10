from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RoomType(models.Model):
    name = models.CharField(verbose_name='Type of Room', max_length=100)
   
    def __str__(self):
        return self.name
    
    
class BedSize(models.Model):
    name = models.CharField(verbose_name='Bed Size', max_length=100)
   
    def __str__(self):
       return self.name
   
   
   
class Room(models.Model):
    room_name = models.CharField(verbose_name='Room Name', max_length=100,default=False)
    room_number = models.CharField(verbose_name='Room Number',max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE) 
    room_bed = models.ForeignKey(BedSize,on_delete=models.CASCADE)
    room_decription = models.TextField(verbose_name='Room Description', default=False)
    price = models.DecimalField(verbose_name='Room Price', max_digits=10, decimal_places=2)
    is_available = models.BooleanField(verbose_name='Room Status', default=True)
    photo = models.ImageField(verbose_name='Image of room', upload_to='photo/%Y/%m/%d/', default='/photo/2024/06/14/empty.png')
    
    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"
  

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField(verbose_name='Check in')
    check_out = models.DateTimeField(verbose_name='Check out')
    number_of_guests = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Reservation by {self.user.username}"
 
    
class HotelInfo(models.Model):
    name = models.CharField(verbose_name="Hotel Name", max_length=100)
    description = models.TextField(verbose_name='Hotel Description')
    address = models.CharField(verbose_name='Hotel Address',max_length=255)
    phone = models.CharField(verbose_name='Hotel Phone Number',max_length=20)
    
    def __str__(self):
        return self.name
