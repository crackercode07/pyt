from django.contrib import admin
from .models import product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(product, ProductAdmin)

