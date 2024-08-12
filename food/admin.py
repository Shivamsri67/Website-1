from django.contrib import admin

from .models import item
@admin.register(item)
class itemadmin(admin.ModelAdmin):
    list_display=['id','name','desc','price','image']
    search_fields=['name','price']
                
                

                
        
