from django.db import models
from items.models import BaseItem, Item
from inventory.users.models import User
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=40, unique=True)
    TYPE_CHOICES = (
        ('Warehouse', 'Warehouse'),
        ('Store', 'Store'),
        ('Refurbish/Recycling Center/Landfill',
         'Refurbish/Landfill/Recyling center'),
        ('supplier', 'Supplier')
    )
    type = models.CharField(max_length=35, choices=TYPE_CHOICES)
    address = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return "%s - %s" % (self.type, self.name)

    class Meta:
        ordering = ('name',)


class Transaction(models.Model):
    item = models.ForeignKey(BaseItem, related_name='transactions')
    date_time = models.DateTimeField(auto_now_add=True)
    items_count = models.IntegerField(null=True, blank=True)
    origin = models.ForeignKey(Location, related_name='origins')
    destination = models.ForeignKey(Location, related_name='destinations')
    owner = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        Item.objects.filter(base_item__id=self.item.id, location=self.origin)\
        .order_by('expiration_date')\
        .update(location=self.destination)[:self.items_count]
        super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = ('date_time',)

