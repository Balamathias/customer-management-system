from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

from .decorators import *
from django.forms import inlineformset_factory
from .filters import OrderFilter

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group


# Create your views here.

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['customers'])
def user(request):
    orders = request.user.customer.order_set.all()
    total_delivered = orders.filter(status='delivered').count()
    total_pending = orders.filter(status='pending').count()
    orderlist = orders.count()
    context = {
        'orders': orders,
        'orderlength': orderlist,
        'total_delivered': total_delivered,
        'total_pending': total_pending,
    }
    return render(request, 'user.html', context)

@unauthenticated_user
#@allowed_users(allowed_roles=['admin'])
def register_page(request):   
    form = CreatedFormUser() 
    if request.method:
        form = CreatedFormUser(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Welcome ' + username +', Your account was created successfully.')
            return redirect('login')
        
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


@unauthenticated_user
#@allowed_users(allowed_roles=['admin'])
def login_page(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password does not exist.')

    return render(request, 'login.html') 

    
def log_out(request):
    logout(request)
    return redirect('login')
    
    
@login_required(login_url='login')
@admin_only
def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    # order = customers.order_set.all()
    total_delivered = orders.filter(status='delivered').count()
    total_pending = orders.filter(status='pending').count()
    orderlist = orders.count()
    
    context = {
        'customers': customers,
        'orders': orders,
        'orderlength': orderlist,
        'total_delivered': total_delivered,
        'total_pending': total_pending,
    }
    return render(request, 'dashboard.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()    
    return render(request, 'products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def account_setting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'account_setting.html', context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('status','product'), extra=5)
    formset = OrderFormSet( queryset = Order.objects.none(),instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
        return redirect('/')
    context = {
        'formset':formset,    
        'customer': customer
    }
    return render(request, 'addorder.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'addorder.html', context)

    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    
    order_count = orders.count()
    return render(request, 'customers.html', {'orders':orders, 'customer': customer, 'order_count': order_count, 'my_filter': my_filter})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    return render(request, 'delete.html', {'order':order})






# @login_required(login_url='/login')
# @allowed_users(allowed_roles=['admin'])
# def add(request):
#     return render(request, 'add.html')


# def addcustomer(request):
    
#     name = request.POST['username']
#     phone = request.POST['phone']
#     customer = Customer.objects.create(name=name, phone=phone)
#     customer.save()
#     return redirect('/')