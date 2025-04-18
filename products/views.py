from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'إضافة منتج'})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user and not request.user.is_superuser:
        return redirect('dashboard')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'تعديل منتج'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user and not request.user.is_superuser:
        return redirect('dashboard')
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

