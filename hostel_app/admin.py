from django.contrib import admin

from hostel_app.models import Guest
from hostel_app.models import Room
from hostel_app.models import Booking
from hostel_app.models import Staff
from hostel_app.models import Duty, Subscriber



@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone","score")
    search_fields = ("name", "age","phone")
    list_filter = ("score", )
    fields = ('name','age','phone',"score")

    
@admin.register(Room)
class Room2Admin(admin.ModelAdmin):
    list_display = ("name", "price", 'hottest','bed','bath')
    search_fields = ("name", "price",)
    list_filter = ("is_booked", 'hottest')
    fields = ('name','description','price','is_booked','img', 'hottest','bed','bath')
    list_editable = ('hottest',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "room","checkin_date", "checkout_date",)
    readonly_fields = ("is_checkout",)
    search_fields = ("name", "is_checkout",)
    list_filter = ("room", )
    fields = ('name','room','num_of_guest','num_of_child','phone','checkin_date','checkout_date','is_checkout')
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "data","phone","post")
    search_fields = ("name", "data","post")
    list_filter = ("post", )
    fields = ('name','data','passport',"address","phone","post","login","password", 'img')
    

@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ("staff", "day")
    search_fields = ("day",)
    list_filter = ("day", )
    fields = ('staff','day')
    
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ('email',)
