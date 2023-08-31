from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cart, CartItem, User

class CartItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CartItemForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = CartItem
        exclude = ("cart", "product")

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




