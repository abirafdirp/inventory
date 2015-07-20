from django.forms import ModelForm
from .models import BaseItem
from .models import Item
from .models import ProductIdPrefix
from .models import Brand
from .models import Category

class BaseItemForm(ModelForm):
    class Meta:
        model = BaseItem
        exclude = ['owner']

