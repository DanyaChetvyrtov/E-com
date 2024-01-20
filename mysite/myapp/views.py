from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


def index(request):
    items = Product.objects.all()
    context = {
        "items": items,
    }
    return render(request, "myapp/index.html", context)


def index_item(request, correct_product_id):
    item = Product.objects.get(id=correct_product_id)
    context = {
        "item": item,
    }
    return render(request, "myapp/detail.html", context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("upload")
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/add_item.html")


def update_item(request, correct_product_id):
    item = Product.objects.get(id=correct_product_id)

    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/")
    context = {"item": item}
    return render(request, "myapp/update_item.html", context)


def delete_item(request, correct_product_id):
    item = Product.objects.get(id=correct_product_id)

    if request.method == "POST":
        item.delete()
        return redirect("/myapp/")

    context = {"item": item}
    return render(request, "myapp/delete_item.html", context)
