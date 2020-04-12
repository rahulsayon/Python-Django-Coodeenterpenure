from django.http import Http404
from django.shortcuts import render
from .models import Product
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from . forms import ProductForm,RawProductForm


def product_details_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title':obj.title,
        'description':obj.description
    }
    return render(request,"products/detail.html",context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
    return render(request,"products/product_create.html",context)


# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print("sssss",form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
    
#     context = {
#         "form" : form
#     }
#     return render(request,"products/product_create.html",context)

def render_initial_data(request,id):
    initial_data = {
        "title":"My this awesome title"
    }
    obj = Product.objects.get(id=id)
    form  = ProductForm(request.POST or None , initial=initial_data,instance=obj)
    if form.is_valid():
        form.save()
    context = { "form" : form }
    return render(request,"products/product_create.html",context)

def dynamic_lookup_view(request,id):
    # obj = Product.objects.get(id=slug)
    # obj = get_object_or_404(Product,id=slug)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj":obj
    }
    return render(request,"products/product_details.html",context)


def product_delete_view(request,slug):
    obj = Product.objects.get(id=1)
    obj.delete()
    return redirect("../../")

    context = {
         "obj":obj
    }
    return render(request,"products/product_delete.html",context)

def product_list_view(request):
    obj = Product.objects.all()
    context = {
         "obj":obj
    }
    return render(request,"products/product_list.html",context)