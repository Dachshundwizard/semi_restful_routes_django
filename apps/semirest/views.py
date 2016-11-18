from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product

def index(request):
    try:
            products = Product.objects.all()
            context = {
                    'products': products
            }
    except NameError:
        context = {}

    return render(request, 'semirest/index.html', context)


def show(request, id):
    context = {
            'product' : Product.objects.get(id = id)
    }
    return render(request, 'semirest/show.html, context')

def new(request):
    return render(request, 'semirest/new.html')

def edit(request, id):
    context = {
            'product' : Product.objects.get(id = id)
    }
    return render(request, 'semirest/edit.html', context)

def create(request):
    new_product = Product.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
    return redirect(reverse('semirest:index'))

def update(request, id):
	new_product = Product.objects.get(id = id)
	new_product.name = request.POST['name']
	new_product.description = request.POST['description']
	new_product.price = request.POST['price']
	new_product.save()
	return redirect(reverse('semirest:index'))

def destroy(request, id):
	Product.objects.filter(id = id).delete()
	return redirect(reverse('semirest:index'))
