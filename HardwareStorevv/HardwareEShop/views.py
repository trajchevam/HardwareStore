from django.shortcuts import render
from .models import Product, CartItem, Cart
from .forms import CartItemForm

# Create your views here.
def index(request):
    querryset = Product.objects.all()
    context = {"products": querryset}
    return render(request,'index.html', context=context)

def products(request):
    querryset = Product.objects.all()
    context = {"products": querryset}
    return render(request,'products.html', context=context)

def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {"cart_items": cart_items}

    return render(request,'cart.html', context=context)

def addCartItem (request, product_id):

    if request.method == "POST":
        form = CartItemForm(request.POST)
        if form.is_valid():
            cartItem = form.save(commit=False) #ostavame mozhnost da napravime override na polinjata
            cart = Cart.objects.get(user=request.user)
            cartItem.cart = cart
            product = Product.objects.get(id = product_id)
            cartItem.product = product
            cartItem.save()
    else:
        form = CartItemForm()

    return render(request, "addCartItem.html", {"form": form})

def deleteCartItem(request, cart_item_id):
    CartItem.objects.get(id = cart_item_id).delete()
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {"cart_items": cart_items}

    return render(request,'cart.html', context=context)
