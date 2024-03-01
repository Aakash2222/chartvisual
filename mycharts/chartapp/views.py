from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.
def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()



    context= {
        "products": products,
        "form": form,
    }
    return render(request, 'chartapp/index.html',context)
