import json
from django import template
from items.models import Item
from items.models import BaseItem
from transaction.models import Transaction
from transaction.models import Location

register = template.Library()

@register.assignment_tag
def get_items_in_locations():
    items_in_a_location = {}
    counter = 1
    lastlocation = ''
    lastitem = ''
    items = Item.objects.all()
    for item in items:
        if str(item.location) != lastlocation:
            counter = 1
        if str(item.baseitem.name) != lastitem:
            items_in_a_location['name'] = item.base_item.name
        items_in_a_location[str(item.location)] = counter
        lastlocation = str(item.location)
        lastitem = str(item.base.item.name)
        counter += 1
    return json.JSONEncoder().encode(items_in_a_location)

@register.assignment_tag
def get_items_in_locationss():
    for location in Location.objects.all():
        location.ite
