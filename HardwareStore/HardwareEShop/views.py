from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, CartItem, Cart
from .forms import CartItemForm, SignUpForm

# Create your views here.
def index(request):
    querryset = Product.objects.all()
    user = request.user
    context = {"products": querryset, "user": user}
    return render(request,'index.html', context=context)

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})
def products(request):
    querryset = Product.objects.all()
    context = {"products": querryset}
    return render(request,'products.html', context=context)

@login_required
def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    all = 0

    for cart_item in cart_items:
       all += cart_item.product.price * cart_item.quantity

    context = {"cart_items": cart_items, "sum": all}

    return render(request,'cart.html', context=context)

@login_required
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
            return redirect('index')
    else:
        form = CartItemForm()

    return render(request, "addCartItem.html", {"form": form})

@login_required
def addQuantityOfCartItem(request, cart_item_id):
    cart_item = CartItem.objects.get(id = cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def removeQuantityOfCartItem(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item.quantity == 1:
        CartItem.objects.get(id=cart_item_id).delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')

@login_required
def deleteCartItem(request, cart_item_id):
    CartItem.objects.get(id = cart_item_id).delete()
    return redirect('cart')

@login_required
def account(request):
    context = {"user": request.user}
    return render(request,'account.html', context=context)
