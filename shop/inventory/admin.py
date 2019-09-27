from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'unit_price',
        'quantity',
        'status',
        'issues',
    ]



admin.site.site_header = "Simple Shop"
admin.site.site_title = "Simple Shop"
admin.site.register(Product, ProductAdmin)

