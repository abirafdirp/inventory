from django.db import models
from items.models import Item
from inventory.users.models import User
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=40)
    TYPE_CHOICES = (
        ('Warehouse', 'Warehouse'),
        ('Store', 'Store'),
        ('Refurbish/Recycling Center/Landfill', 'Refurbish/Landfill/Recyling center'),
        ('supplier', 'Supplier')
    )
    type = models.CharField(max_length=35, choices=TYPE_CHOICES)
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(User)

    def __str__(self):
        return "%s - %s" % (self.type, self.name)

class Transaction(models.Model):
    items = models.ManyToManyField(Item)
    date_time = models.DateTimeField(auto_now_add=True)
    items_in = models.IntegerField(null=True, blank=True)
    items_out = models.IntegerField(null=True, blank=True)
    origin = models.ForeignKey(Location, null=True, blank=True,
                               related_name='origin_of')
    destination = models.ForeignKey(Location, null=True, blank=True,
                                    related_name='destination_of')
    owner = models.ForeignKey(User)



