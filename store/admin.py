from django.contrib import admin
from .models import*
# Register your models here.
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','price')
#     # prepopulated_fields = {'slug': ('name',)}
 
admin.site.register(Order)
# admin.site.register(Order)