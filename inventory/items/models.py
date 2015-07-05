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

class Item(NameModel, TimeStampedModel):
    brand = models.ForeignKey(Brand, related_name='brand_of')
    category = models.ManyToManyField(Category, related_name='category_of')
    description = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='items', blank=True)
    expireable = models.BooleanField(default=False)
    expires_on = models.DateField(null=True, blank=True)

    #prevent circular import
    location = models.ForeignKey('transaction.Location', related_name='location_of')

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.today()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
