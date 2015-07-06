from django.db import models
import datetime
# Create your models here.

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

class ProductIdPrefix(NameModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product ID Prefixes"

class BaseItem(NameModel, TimeStampedModel):
    sku = models.CharField(max_length=20, verbose_name='SKU')
    brand = models.ForeignKey(Brand, related_name='brand_of')
    category = models.ManyToManyField(Category, related_name='category_of')
    description = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='items', blank=True)
    expireable = models.BooleanField(default=False)
    expires_in = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.today()
        super(BaseItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Item(TimeStampedModel):
    base_item = models.ForeignKey(BaseItem, related_name='base_item_of')

    # the product id will be randomly generated from its prefix
    product_id_prefix = models.ForeignKey(ProductIdPrefix, null=True)
    product_id = models.CharField(max_length=15,
                                  help_text='Randomly generated from Product ID Prefix'+
                                            ' if left blank. max length 15 chars')
    expired = models.BooleanField(default=False)

    # prevent circular import
    location = models.ForeignKey('transaction.Location', related_name='location_of')

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.today()

        if not self.product_id_prefix:

        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.base_item.name


