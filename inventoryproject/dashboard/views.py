from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
#@login_required(login_url='user-login')
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders' : orders,
        'form': form,
        'products' : products, 
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    context={
        'workers' : workers

    }
    return render(request, 'dashboard/staff.html', context)
@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context={
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    """
    Handles the display and creation of products.

    GET: Displays all products and an empty product form.
    POST: Processes the product form, validates it, and saves the product.
    Provides appropriate success or error messages.
    """
    # Fetch all product records using the ORM
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Save the new product and fetch the product name
            product = form.save()
            product_name = product.name
            messages.success(request, f'Product "{product_name}" has been successfully added!')
            return redirect('dashboard-product')
        else:
            # Handle invalid form submission
            messages.error(request, 'Failed to add the product. Please check the form for errors.')
    else:
        form = ProductForm()

    # Provide feedback if no products exist
    if not products.exists():
        messages.info(request, 'No products are currently available. Start by adding a new product!')

    context = {
        'items': products,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context={
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
    orders = Order.objects.all()

    context ={
        'orders': orders,
    }
    return render(request, 'dashboard/order.html', context)

