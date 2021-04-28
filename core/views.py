from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

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
    }
    return render(request, 'index.html', context)

def dichvu_view(request):
    return render(request, 'dichvu.html', {})

def bangtuongtac_view(request):
    objs = Product.objects.all()
    context = {
        'objects': objs
    }
    return render(request, 'bangtuongtac.html', context)

def dichvubaotribaohanhmay_view(request):
    return render(request, 'dichvubaotribaohanhmay.html', {})

def dichvuthuemayphotocopy_view(request):
    return render(request, 'dichvuthuemayphotocopy.html', {})

def giohang_view(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = { 'get_cart_total':0 }

    context = {
        'items':items, 
        'order':order,
        'cartItems':cartItems,
    }
    return render(request, 'giohang.html', context)

def manhinhghep_view(request):
    return render(request, 'manhinhghep.html', {})

def maychieu_view(request):
    return render(request, 'maychieu.html', {})

def mayphoto_view(request):
    objs = Product.objects.all()
    context = {
        'objects': objs
    }
    return render(request, 'mayphoto.html', context)

def tintuc_view(request):
    return render(request, 'tintuc.html', {})

def vechungtoi_view(request):
    return render(request, 'vechungtoi.html', {})

def printscan_view(request):
    return render(request, 'printScan.html', {})

def thongbaobaotrimay_view(request):
    return render(request, 'thongbaobaotrimay.html', {})

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

    if orderitem.quantity <= 0:
        orderitem.delete()
    
    return JsonResponse('Item was added', safe=False)
