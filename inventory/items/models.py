import random
import string
import datetime
from django.db import models
from django.utils import timezone
from inventory.users.models import User

# Create your models here.
class Owner(models.Model):
    """
    Abstract model class that provide
    owner field for authentication in REST
    """

    owner = models.ForeignKey(User)

    class Meta:
        abstract = True

class TimeStampedModel(models.Model):
    """
    Abstract model class that provides
    self-updating 'created' and 'modified'
    fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class NameModel(models.Model):
    """
    Abstract model class that provides
    name.
    """

    name = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Brand(NameModel, TimeStampedModel):
    """
    Brand of an item.
    """
    def __str__(self):
        return self.name

class Category(NameModel, TimeStampedModel):
    """
    Category of an item.
    """
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class ProductIdPrefix(models.Model):
    name = models.CharField(max_length=7, help_text='Max length 7 characters')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product ID Prefixes"

class BaseItem(NameModel, TimeStampedModel):
    sku = models.CharField(max_length=20, verbose_name='SKU')
    product_id_prefix = models.ForeignKey(ProductIdPrefix, null=True, blank=True,
                                          verbose_name='Product ID prefix')
    brand = models.ForeignKey(Brand, related_name='brand_of')
    category = models.ManyToManyField(Category, related_name='category_of')
    description = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='items', blank=True)
    expireable = models.BooleanField(default=False)
    expires_in = models.IntegerField(null=True, blank=True, default=0, verbose_name='Expires in (days)',
                                  help_text='This is NOT expiration date, but how long until '+
                                  'this item will be expired in days. Leave blank if the item'+
                                  ' is not expireable')

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.today()
        if self.expires_in == 0:
            self.expireable = False
        else:
            self.expireable = True
        super(BaseItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Item(TimeStampedModel):
    base_item = models.ForeignKey(BaseItem, related_name='base_item_of')

    # the product id will be randomly generated from its prefix
    # because the product ID is given by the supplier
    product_id = models.CharField(max_length=15, blank=True,
                                  help_text='Product ID will be generated randomly to '+
                                'simulate shipment from supplier'
                                )
    expiration_date = models.DateField(editable=False, blank=True)
    expired = models.BooleanField(default=False)

    # prevent circular import
    location = models.ForeignKey('transaction.Location', related_name='location_of')

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        expires_in = self.base_item.expires_in
        if expires_in == 0:
            self.expiration_date = datetime.datetime(2099, 12, 12)
        else:
            self.expiration_date = timezone.now() + datetime.timedelta(days=expires_in)

        # randomized product id, 7 chars from the max length of SKU
        # and 8 chars is randomized. Max len of product id is 15 chars
        # if there is already one, then it will continue to be randomized
        while True:
            product_ID = self.base_item.product_id_prefix.name + randomword(8)
            try:
                Item.objects.get(product_id = product_ID)
            except:
                self.product_id = product_ID
                break
        super(Item, self).save(*args, **kwargs)

    class Meta:
        ordering = ('expiration_date',)

    def __str__(self):
        return self.base_item.name

def randomword(length):
    return ''.join(random.choice(string.lowercase+string.digits) for i in range(length))