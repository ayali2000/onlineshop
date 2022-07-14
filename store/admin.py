from django.contrib import admin
from . models import *

# Register your models here.
class AdminItems(admin.ModelAdmin):
    list_display = ['Name','Category','Description','Location','Price','date_added']
    
admin.site.register(Items,AdminItems)

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['Name','Phone_num','Address','Product_name','Quantity']
    
admin.site.register(OrderItem,AdminOrderItem)


