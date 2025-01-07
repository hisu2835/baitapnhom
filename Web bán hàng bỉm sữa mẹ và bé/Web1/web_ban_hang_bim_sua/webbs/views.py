from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product, Customer, Cart, Order, OrderItem, CartItem

def home(request):
    return HttpResponse("Hello world!")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(customer=request.user.customer)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_object_or_404(Cart, customer=request.user.customer)
    return render(request, 'cart_detail.html', {'cart': cart})

def order_create(request):
    cart = get_object_or_404(Cart, customer=request.user.customer)
    order = Order.objects.create(customer=request.user.customer, total_amount=cart.get_total_price())
    for item in cart.cartitem_set.all():
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
    cart.cartitem_set.all().delete()
    return redirect('order_detail', order_id=order.id)

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})