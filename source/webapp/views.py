from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import SearchForm, ProductForm


def index_view(request):
    products = Product.objects.filter(amount__gt=0).order_by('category', 'name')
    search_form = SearchForm()
    return render(request, 'index.html', context={
        'products': products,
        'search_form': search_form
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })


def search_by_name(request, *args, **kwargs):
    search = request.GET.get('search')
    products = Product.objects.filter(name__contains=search)
    form = SearchForm()
    return render(request, 'index.html', context={
        'products': products,
        'form': form,
    })


def product_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price'],
            )
            return redirect('product_detail', pk=product.pk)
        else:
            return render(request, 'product_create.html', context={
                'form': form
            })


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'amount': product.amount,
            'price': product.price
        })
        return render(request, 'update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.amount = form.cleaned_data['amount']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product_detail', pk=product.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'product': product})

