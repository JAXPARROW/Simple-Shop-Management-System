from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'unit_price',
        'quantity',
        'status',
        'active',
        'created',
        'updated',
        # 'issues',
    ]
    search_fields = [
        'product_name',

    ]

    list_editable = [
        # 'product_name',
        'unit_price',
        'quantity',
        'status',
        'active',
    ]

    list_filter = [
        # 'product_name',
        'status',
        'active'
    ]
     
    list_per_page = 20

    date_hierarchy = 'created'

    readonly_fields = [
        'created',
        'updated'
    ]

    prepopulated_fields = {"slug":("product_name",)}


admin.site.site_header = "Simple Shop"
admin.site.site_title = "Simple Shop"
admin.site.register(Product, ProductAdmin)

