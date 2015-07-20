from djangular.forms import NgFormValidationMixin
from . import forms

class SubscribeForm(NgFormValidationMixin, forms.BaseItemForm):
    # Apart from an additional mixin class, the Form declaration from the
    # 'Classic Subscription' view, has been reused here.
    pass
