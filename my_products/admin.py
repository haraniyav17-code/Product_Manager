from django.contrib import admin
from .models import ProductDetails


# Register your models here.
# admin.site.register(ProductDetails)
@admin.register(ProductDetails)
class AdminProductDetails(admin.ModelAdmin):
    list_display=('id','name','price','description')
    list_filter=('name',)
    
