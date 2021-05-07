from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from  .models import*
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def fruit(request):
    fruits = Fruit.objects.all()
    return render(request,'fruit.html',{'fruits':fruits})

def contact(request):
    if request.method=='POST':
        nm  =request.POST['cname']
        em = request.POST['cemail']
        mn = request.POST['cmobno']
        msg = request.POST['cmessage']
        Contact.objects.create(full_name=nm,email=em,mob_no=mn,message=msg).save()
        messages.success(request,"Your message is Succesfully send!!!")
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def testimonial(request):
    return render(request,'testimonial.html')


def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"congratulations!! Your account is succesfully created")
            fm.save()
    else:
        fm = SignupForm()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass =  fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return redirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return redirect('/home/')

def user_logout(request):
    logout(request)
    return redirect('/home/')


def detail(request,id):
    fd = Fruit.objects.get(id=id)
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(fruits=fd.id) & Q(user=request.user)).exists()
        print(item_already_in_cart)
    else:
        return redirect('/login/')
    d = {'detail': fd, 'item_already_in_cart': item_already_in_cart}
    return render(request, 'detail.html', d)


def add_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('pid')
        product = Fruit.objects.get(id=product_id)
        Cart(user=user,fruits=product).save()

        return redirect('/showcart/')

    return redirect('/login/')

def view_booking(request):
    data = Booking.objects.filter(user=request.user)
    return render(request,'view_booking.html',{'data':data})


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        #print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity* int(p.fruits.price_per_kg))
                amount += (tempamount)
                totalamount = amount+shipping_amount

            return render(request,'cart.html',{'carts':cart , 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request,'emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        c = Cart.objects.get(Q(fruits=pid) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * int(p.fruits.price_per_kg))
            amount += int(tempamount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        add = Customer.objects.filter(user=user)
        if add:
            cart_items = Cart.objects.filter(user=user)
            amount = 0
            shipping_amount = 70
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            if cart_product:
                for p in cart_product:
                    tempamount = (p.quantity * int(p.fruits.price_per_kg))
                    amount += int(tempamount)
                totalamount  = amount+shipping_amount
                return render(request,'checkout.html',{'totalamount':totalamount,'carts':cart_items,'add':add})
        else:
            return redirect('/profile/')
    return redirect('/login/')


def minus_cart(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        c = Cart.objects.get(Q(fruits=pid) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * int(p.fruits.price_per_kg))
            amount += int(tempamount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        c = Cart.objects.get(Q(fruits=pid) & Q(user=request.user))
        c.delete()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * int(p.fruits.price_per_kg))
            amount += int(tempamount)
        data = {
            'amount': amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)

def address(request):
    user= request.user
    add = Customer.objects.filter(user=user)
    return render(request,'address.html',{'add':add,'active':'btn-primary'} )

def profile(request):
    if request.method == 'POST':
        user = request.user
        nm = request.POST['cname']
        mob = request.POST['mobno']
        cit = request.POST['ccity']
        stat = request.POST['cstate']
        zi = request.POST['czip']
        add = request.POST['cAdd']
        Customer.objects.create(user=user, name=nm, mobile_no=mob, city=cit,state=stat,zipcode=zi,addres_s=add)
        messages.success(request,'Your Address is Succesfully Added')
        return render(request,'profile.html',{'active':'btn-primary'})


    return render(request,'profile.html')

def booking(request):
    user = request.user
    bookid = request.GET.get('bookid')
    print(bookid)
    customer = Customer.objects.get(id=bookid)
    print(customer)
    cart = Cart.objects.filter(user=user)
    for  c in cart:
        Booking(user=user,customer=customer,product=c.fruits,quantity=c.quantity).save()

        c.delete()
    return redirect('/viewbooking/')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Fruit.objects.filter(Q(name__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
        else:
            return redirect('/home/')
    return render(request,'index.html')