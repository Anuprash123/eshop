from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    price_per_kg = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Cart(models.Model):
    fruits = models.ForeignKey(Fruit,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



    def __str__(self):
        return str(self.id)




class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=30, null=True)
    mobile_no = models.CharField(max_length=10, null=True)
    addres_s = models.TextField(max_length=100)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
)


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.CharField(max_length=20,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30,
    choices=STATUS_CHOICES,default='pending')
    def __str__(self):
        return self.product

class Contact(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    mob_no = models.CharField(max_length=10)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.full_name


