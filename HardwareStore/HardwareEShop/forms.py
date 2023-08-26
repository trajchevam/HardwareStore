from django import forms
from .models import Cart, CartItem

class CartItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CartItemForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = CartItem
        exclude = ("cart", "product")
