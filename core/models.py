from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    @property
    def changeDefaultAddress(self):
        shipping = self.shippingaddress_set.all()
        for address in shipping:
            address.default = False

"""     @property 
    def changeDefaultAddress(self, id):
        shipping = self.shippingaddress_set.all()
        for address in shipping:
            if address.id == id:
                address.default=True
            else:
                address.default = False """
    

class Product(models.Model):
    MAYPHOTOCOPY = 'MP'
    BANGTUONGTAC = 'BT'
    PRINTSCAN = 'PS'
    MAYCHIEU = 'MC'
    MANHINHGHEP = 'MH'
    PRODUCT_TYPE_CHOICES = [
        (MAYPHOTOCOPY, 'may photocopy'),
        (BANGTUONGTAC, 'bang tuong tac'),
        (PRINTSCAN, 'print scan'),
        (MAYCHIEU, 'may chieu'),
        (MANHINHGHEP, 'man hinh ghep'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="static/images")
    productType = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, default=MAYPHOTOCOPY)
    ship = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_orderd= models.DateTimeField(auto_now_add=True)    
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shippingEligibility(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for orderitem in orderitems: 
            if orderitem.product.ship == True:
                shipping = True        
        return shipping

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, default='None')
    email = models.CharField(max_length=200, default='None')
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)   
    date_added = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.address