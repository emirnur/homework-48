from django.shortcuts import render, get_object_or_404
from webapp.models import Product
from webapp.forms import SearchForm


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


