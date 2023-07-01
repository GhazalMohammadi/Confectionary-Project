from django.shortcuts import render , get_object_or_404 , redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import City , CategoriesOfProducts , Inventory , Warehouse , Product ,Order , OrderItem
from django.views.generic import ListView , UpdateView
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def HomeView(request):
    template = loader.get_template('home.html')
    cities = City.objects.all()
    categories = CategoriesOfProducts.objects.all()
    products = Inventory.objects.all()
    context = {
        'cities':cities,
        'categories':categories,
        'products':products,
    }
    return HttpResponse(template.render( context,request))


def HomeLocationView(request , id_city):
    template = loader.get_template('homeLocation.html')
    cities = City.objects.all()
    categories = CategoriesOfProducts.objects.all()
    products = Inventory.objects.filter(warehouse__city__id = id_city)
    context = {
        'cities':cities,
        'categories':categories,
        'products':products,
    }
    return HttpResponse(template.render( context,request))

def HomeCategoryView(request , id_category):
    template = loader.get_template('homeCategory.html')
    cities = City.objects.all()
    categories = CategoriesOfProducts.objects.all()
    products = Inventory.objects.filter(product__categories__id = id_category)
    context = {
        'cities':cities,
        'categories':categories,
        'products':products,
    }
    return HttpResponse(template.render( context,request))



def AboutView(request):
    template = loader.get_template('about.html')
    cities = City.objects.all()
    context = {
        'cities':cities
    }
    return HttpResponse(template.render( context,request))

def ContactView(request):
    template = loader.get_template('contact.html')
    cities = City.objects.all()
    context = {
        'cities':cities
    }
    return HttpResponse(template.render( context,request))

def ProfileCartView(request , username):
    template = loader.get_template('profileCart.html')
    cities = City.objects.all()
    orders = OrderItem.objects.filter(user__username = username)
    context = {
        'cities':cities , 
        'orders':orders,
    }
    return HttpResponse(template.render( context,request))


class ProfileView(UpdateView):
    model = User
    template_name = 'profile.html'
    fields = ['username' , 'first_name' , 'last_name' , 'email']

def ProfileHistoryView(request , username):
    template = loader.get_template('profileHistory.html')
    cities = City.objects.all()
    context = {
        'cities':cities
    }
    return HttpResponse(template.render( context,request))

class ProfileManagerView(UpdateView):
    model = User
    template_name = 'profileManager.html'
    fields = ['username' , 'first_name' , 'last_name' , 'email']

def ProfileManagerInventory(request , username):
    template = loader.get_template('profileManagerInventory.html')
    cities = City.objects.all()
    orders = Order.objects.all()
    context = {
        'cities':cities ,
        'orders':orders,
    }
    return HttpResponse(template.render( context,request))

def OrderView(request , inventory_id):
    template = loader.get_template('order.html')
    product = get_object_or_404(Inventory , id = inventory_id)
    cities = City.objects.all()
    context = {
        'cities':cities , 
        'product':product,
    }
    return HttpResponse(template.render( context,request))



def add_to_cart(request , inventory_id):
    product = get_object_or_404(Inventory , id =inventory_id )
    order_item , created = OrderItem.objects.get_or_create(product = product , user=request.user , ordered = False)
    order_qs = Order.objects.filter(user=request.user , ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item  is in the order
        if order.products.filter(product_id = product.id).exists() :
            order_item.quantity += 1
            order_item.save()
            messages.info(request , 'تعداد محصول افزایش یافت')
        else:
            messages.info(request , 'محصول به سبد اضافه شد')
            order.products.add(order_item)
            return redirect('/'+str(inventory_id)+'/Product/')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user , ordered_date=ordered_date)
        order.products.add(order_item)
        messages.info(request , 'محصول به سبد اضافه شد')

    return redirect('/'+str(inventory_id)+'/Product/')


def  remove_from_cart(request , inventory_id):
    product = get_object_or_404(Inventory , id =inventory_id )
    order_qs = Order.objects.filter(user=request.user , ordered=False)
    order_item , created = OrderItem.objects.get_or_create(product = product , user=request.user , ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item  is in the order
        if order.products.filter(product_id = product.id).exists() :
            order.products.remove(order_item)
            messages.info(request , 'محصول از سبد حذف شد')
            return redirect('/'+str(inventory_id)+'/Product/')
        else:
            messages.info(request , 'این محصول در سبد شما نیست')
            return redirect('/'+str(inventory_id)+'/Product/')

    else:
        messages.info(request , 'سفارشی در سبد موجوذ نیست')
        return redirect('/'+str(inventory_id)+'/Product/')
        




