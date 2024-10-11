from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    """Контроллер для домашней страницы."""
    return render(request, "home.html")


def contacts(request):
    """Контроллер для отображения страницы с контактной информацией."""
    if request.method == "POST":
        name = request.POST.get("name")
        massage = request.POST.get("massage")
        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")
    return render(request, "contacts.html")


def product_list(request):
    """Контроллер для отображения продуктов"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
