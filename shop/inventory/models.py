from django.db import models
from datetime import datetime

class Product(models.Model):
    
    product_name = models.CharField(max_length=200, blank=False)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    choices = (
        ('AVAILABLE', 'ITEM AVAILABLE'),
        ('SOLDOUT', 'ITEM SOLDOUT'),
        ('RESTOCKING', 'RESTOCKING IN FEW DAYS')
    )

    status = models.CharField(max_length=10, choices=choices, default='AVAILABLE')
    issues = models.CharField(max_length=50, default="No Issues")
    

    # class Meta:
    #     abstract = False

    def __str__(self):
        return self.product_name