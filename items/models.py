import random
import string
import datetime
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from inventory.users.models import User

# Create your models here.
"""class Owner(models.Model):
    ""
    Abstract model class that provide
    owner field for authentication in REST
    ""

    owner = models.ForeignKey(User)

    class Meta:
        abstract = True"""


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

    name = models.CharField(max_length=30, unique=True)

    class Meta:
        abstract = True


class Brand(NameModel, TimeStampedModel):

    """
    Brand of an item.
    """

    owner = models.ForeignKey(User, related_name='brands')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Category(NameModel, TimeStampedModel):

    """
    Category of an item.
    """

    owner = models.ForeignKey(User, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

class BaseItem(NameModel, TimeStampedModel):
    sku = models.CharField(max_length=20, verbose_name='SKU', unique=True,
                           help_text='must be unique')
    product_id_prefix = models.CharField\
        (unique=True, verbose_name='Product ID prefix', max_length=7,
         help_text='must be unique, max length 7 characters')
    brand = models.ForeignKey(Brand, related_name='baseitems')
    category = models.ManyToManyField(Category, related_name='baseitems')
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='items', null=True, blank=True)
    expires_in = models.IntegerField\
        (null=True, blank=True, verbose_name='Expires in (days)',
         help_text='this is NOT expiration date, but how long until ' +
         'this item will be expired in days. Leave blank if the item' +
         ' is not expireable')
    owner = models.ForeignKey(User, related_name='baseitems')

    def save(self, *args, **kwargs):
        self.modified = timezone.datetime.today()
        super(BaseItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Item(TimeStampedModel):
    base_item = models.ForeignKey(BaseItem, related_name='items')

    # the product id will be randomly generated from its prefix
    # the uniqueness will be guaranteed at overrided save method
    product_id = models.CharField\
        (max_length=15, blank=True,
         help_text='left blank to randomize based on product ID prefix')

    expiration_date = models.DateField()
    expired = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='items')

    # prevent circular import
    location = models.ForeignKey('transaction.Location',
                                 related_name='items')

    def save(self, *args, **kwargs):
        self.modified = timezone.now()

        # if expires_in is blank then the expiration dat will be fixed at
        # 2099-12-12
        expires_in = self.base_item.expires_in
        if expires_in == 0 or expires_in is None:
            self.expiration_date = datetime.date(2099, 12, 12)
        else:
            self.expiration_date = timezone.localtime(now()).date() + \
                                   datetime.timedelta(days=expires_in)


        # randomized product id, 7 chars is from product ID
        # prefix and 8 chars is randomized. Max len of product id is
        # 15 chars, if there is already one, then it will continue to
        # be randomized
        random_len = 15 - len(self.base_item.product_id_prefix)
        if self.product_id == '':
            while True:
                product_id = self.base_item.product_id_prefix +\
                             randomword(random_len)
                try:
                    Item.objects.get(product_id=product_id)
                except:
                    self.product_id = product_id
                    break
        super(Item, self).save(*args, **kwargs)

    class Meta:
        ordering = ('expiration_date',)

    def __str__(self):
        return self.base_item.name


def randomword(length):
    return ''.join(random.choice(string.lowercase+string.digits) \
                   for i in range(length))

