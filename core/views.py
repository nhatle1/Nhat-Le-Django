from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import *

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False, 
    }
    return render(request, 'index.html', context)

def dichvu_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
    }
    return render(request, 'dichvu.html', context)

def bangtuongtac_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    objs = Product.objects.all()
    context = {
        'order':order,
        'cartItems':cartItems,
        'objects': objs,
        'shipping':False,
    }
    return render(request, 'bangtuongtac.html', context)

def dichvubaotribaohanhmay_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
    }
    return render(request, 'dichvubaotribaohanhmay.html', context)

def dichvuthuemayphotocopy_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
    }
    return render(request, 'dichvuthuemayphotocopy.html', context)

def giohang_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        if customer.shippingaddress_set.exists():
            addresses = customer.shippingaddress_set.all()
            have_address=True
        else:
            addresses = []
            have_address=False
    else:
        items = []
        order = { 'get_cart_total':0 }

    context = {
        'items':items, 
        'order':order,
        'cartItems':cartItems,
        'customer': customer,
        'shipping':False,
        'addresses': addresses,
        'have_address': have_address,
    }
    return render(request, 'giohang.html', context)

def manhinhghep_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    objs = Product.objects.all()
    context = {
        'order':order,
        'cartItems':cartItems,
        'objects': objs,
        'shipping':False,
    }
    return render(request, 'manhinhghep.html', context)

def maychieu_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    objs = Product.objects.all()
    context = {
        'order':order,
        'cartItems':cartItems,
        'objects': objs,
        'shipping':False,
    }
    return render(request, 'maychieu.html', context)

def mayphoto_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    objs = Product.objects.all()
    context = {
        'order':order,
        'cartItems':cartItems,
        'objects': objs,
        'shipping':False,
    }
    return render(request, 'mayphoto.html', context)

def tintuc_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
    }
    return render(request, 'tintuc.html', context)

def vechungtoi_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
    }
    return render(request, 'vechungtoi.html', context)

def printscan_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    objs = Product.objects.all()
    context = {
        'order':order,
        'cartItems':cartItems,
        'objects': objs,
        'shipping':False,
    }
    return render(request, 'printScan.html', context)

def thongbaobaotrimay_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = { 'get_cart_total':0 }

    context = {
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
    }
    return render(request, 'thongbaobaotrimay.html', context)

def updateItem_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = orderitem.quantity + 1
    elif action == 'remove':
        orderitem.quantity = orderitem.quantity - 1

    orderitem.save()
    if action == 'delete':
        orderitem.delete()
    
    return JsonResponse('Item was added', safe=False)


def checkout_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        if customer.shippingaddress_set.exists():
            addresses = customer.shippingaddress_set.all()
            have_address=True
        else:
            addresses = []
            have_address=False
    else:
        items = []
        order = { 'get_cart_total':0 }
        cartItems = order['get_cart_items']

    context = {
        'items':items,
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
        'addresses':addresses,
        'have_address':have_address,
    }
    return render(request, 'checkout.html', context)


def shipping_info_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        if customer.shippingaddress_set.exists():
            addresses = customer.shippingaddress_set.all()
            have_address=True
        else:
            addresses = []
            have_address=False
    else:
        items = []
        order = { 'get_cart_total':0 }
        cartItems = order['get_cart_items']


    context = {
        'items':items,
        'order':order,
        'cartItems':cartItems,
        'shipping':False,
        'customer':customer,
        'addresses':addresses,
        'have_address':have_address,
    }
    return render(request, 'shippinginfo.html', context)

def updateAddress_view(request):
    if (request.method == "POST"):
        print(request.POST)
    data = json.loads(request.body)
    print(data)
    if request.user.is_authenticated:
        name = data['form']['name']
        email = data['form']['email']
        address = data['shipping']['address']
        city = data['shipping']['city']
        defaultValue = data['shipping']['default']
        default = False
        customer = request.user.customer
        addresses = customer.shippingaddress_set.all()
        if defaultValue == 'True':
            default = True
            for addr in addresses:
                addr.default = False
                addr.save()
            
        ShippingAddress.objects.create(
            customer=customer, 
            address=address,
            city=city,
            default=default,
            name=name,
            email=email,
        )
    return JsonResponse("Nhat Le", safe=False)


def changeDefaultAddress_view(request):
    data = json.loads(request.body)
    defaultId = int(data['defaultId'])
    print(data)
    customer = request.user.customer
    addresses = customer.shippingaddress_set.all()
    for addr in addresses:
        print(addr.id)
        if addr.id == defaultId:
            addr.default = True
        else:
            addr.default = False
        addr.save()
    return JsonResponse("Nhat Le", safe=False)


""" def completingOrder_view(request):
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        address = ShippingAddress.objects.get(default=True)
        order.shippingaddress = address
        if int(data['total']) == order.get_cart_total:
            order.complete = True
        order.save()
    return JsonResponse("Nhat le", safe=False)
 """

def register_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            login(response, new_user)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            customer = Customer.objects.create(user=new_user, name=name, email=email)
            return redirect('/')
    form = RegisterForm()
    return render(response, "register.html", {'form': form})
