from django.views.generic.edit import FormView
from .forms import BaseItemForm

class BaseItemView(FormView):
    template_name = 'forms/create_base_item.html'
    form_class = BaseItemForm
    success_url = '/dashboard/'