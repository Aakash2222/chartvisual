from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

from django.http import JsonResponse

def index(request):
    products = Product.objects.all()

    paginator = Paginator(products,8)
    page = request.POST.get('page')
    paged_products = paginator.get_page(page)

    if request.method == 'POST':
        form = ProductForm(request.POST) 
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    context= {
        "products":paged_products,
        "form": form,
    }
    return render(request, 'chartapp/index.html',context)


# def index(request):
#     products = Product.objects.all()
#     if request.method == 'POST':
#         form = ProductForm(request.POST) 
#         if form.is_valid():
#             form.save()
#     else:
#         form = ProductForm()
#     context= {
#         "products": products,
#         "form": form,
#     }
#     return render(request, 'chartapp/index.html',context)

def signup(request):
    if request.method == "POST":
        form    = SignupForm(request.POST)
        if form.is_valid():
            username    = form.cleaned_data['username']
            email       = form.cleaned_data['email']
            password    = form.cleaned_data['password']
            user = User.objects.create_user(username=username,email=email,password=password,)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    context = {
        'form':form,
    }
    return render(request, 'chartapp/signup.html',context)

def login(request):
    return render(request, 'chartapp/login.html' )


# To save Json data into django model
@csrf_exempt
def save_json(request):
    if request.method == 'POST':
        json_data       = json.loads(request.body)
        
        for obj in json_data:
                   
            # end_year    = int(obj.get('end_year'))
            end_year    = obj.get('end_year')
            intensity   = int(obj.get('intensity')) if obj.get('intensity') != '' else None
            sector      = obj.get('sector')
            topic       = obj.get('topic')
            insight     = obj.get('insight')
            url         = obj.get('url')
            region      = obj.get('region')
            start_year  = obj.get('start_year')
            impact      = int(obj.get('impact')) if obj.get('impact') != '' else None
            added       = obj.get('added')
            published   = obj.get('published')
            country     = obj.get('country')
            relevance   = int(obj.get('relevance')) if obj.get('relevance') != '' else None
            pestle      = obj.get('pestle')
            source      = obj.get('source')
            title       = obj.get('title')
            likelihood  = int(obj.get('likelihood')) if obj.get('likelihood') != '' else None

            products    = Product.objects.create(
                                end_year=end_year,
                                intensity=intensity,
                                sector=sector,
                                topic=topic,
                                insight=insight,
                                url=url,
                                region=region,
                                start_year=start_year,
                                impact=impact,
                                added=added,
                                published=published,
                                country=country,
                                relevance=relevance,
                                pestle=pestle,
                                source=source,
                                title=title,
                                likelihood=likelihood)
        return HttpResponse('JSON DATA HAS BEEN SAVED SUCCESSFULLY !!!')
    return HttpResponse(status=405)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.filter(Q(end_year__icontains=keyword) | Q(topic__icontains=keyword) |  Q(sector__icontains=keyword))
            product_count = product.count()
            
    context ={
        'products' : product,
        'product_count': product_count,
    }
    return render(request, 'chartapp/searchpage.html', context)


def filter(request):
    products=None
    if request.method == 'POST':
        end_year = request.POST['end_year']
        topic = request.POST['topic']
        sector = request.POST['sector']
        region = request.POST['region']
        source = request.POST['source']
        country = request.POST['country']
        # print(end_year,topic,sector,region,source,country)
        if end_year and topic and sector and region and source and country:
            products = Product.objects.filter(Q(end_year__contains=end_year) & Q(topic__contains=topic) & Q(sector__contains=sector) & Q(region__contains=region) & Q(source__contains=source) & Q(country__contains=country))
        elif end_year and topic and sector and region and source:
            products = Product.objects.filter(Q(end_year__contains=end_year) & Q(topic__contains=topic) & Q(sector__contains=sector) & Q(region__contains=region) & Q(source__contains=source))
        elif end_year and topic and sector and region:
            products = Product.objects.filter(Q(end_year__contains=end_year) & Q(topic__contains=topic) & Q(sector__contains=sector) & Q(region__contains=region))
        elif end_year and topic and sector:
            products = Product.objects.filter(Q(end_year__contains=end_year) & Q(topic__contains=topic) & Q(sector__contains=sector))
        elif end_year and topic:
            products = Product.objects.filter(Q(end_year__contains=end_year) & Q(topic__contains=topic))
        elif end_year:
            products = Product.objects.filter(end_year__contains=end_year)
    context ={
        'products': products,
    }
    return render(request, 'chartapp/filterpage.html', context)

def add_data(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) 
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    content = {
        'form':form,
    }
    return render(request, 'chartapp/add_data.html',content)
    