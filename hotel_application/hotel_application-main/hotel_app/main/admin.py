from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(HotelInfo)
admin.site.register(RoomType)
admin.site.register(BedSize)