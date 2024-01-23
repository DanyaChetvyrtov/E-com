from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Product


# def index(request):
#     items = Product.objects.all()
#     context = {"items": items,}
#     return render(request, "myapp/index.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "myapp/index.html"
    context_object_name = "items"


# def index_item(request, correct_product_id):
#     item = Product.objects.get(id=correct_product_id)
#     context = {"item": item,}
#     return render(request, "myapp/detail.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "item"

@login_required
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
