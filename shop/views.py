import json
from django.shortcuts import render, redirect
from base.views import product
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .filters import ProductFilterForm


# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        #     get customers order
        # get an order if it exists or create one if it doesn't exist'
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        cart_totals = order.get_cart_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cart_items = order['get_cart_items']
        cart_totals = order['get_cart_total']

    category = request.GET.get('category')
    if category == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name__contains=category)
    print(category)
    my_filter = ProductFilterForm(request.GET, queryset=products)
    products = my_filter.qs
    categories = Category.objects.all()

    context = {'products': products, 'categories': categories, 'my_filter': my_filter, 'cart_totals': cart_totals,
               'cart_items': cart_items}
    return render(request, 'shop/store.html', context)


def cart(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        customer = request.user.customer
        #     get customers order
        # get an order if it exists or create one if it doesn't exist'
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False}
        cart_items = order['get_cart_items']
    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        customer = request.user.customer
        #     get customers order
        # get an order if it exists or create one if it doesn't exist'
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cart_items = Order['get_cart_items']
    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'shop/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('p_id:', productID)
    print('action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':

        order_item.quantity = (order_item.quantity - 1)
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('item was added', safe=False)


def detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)


@login_required(login_url='store')
def delete_item(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('store')
    context = {'item': product}
    return render(request, 'shop/delete.html', context)
