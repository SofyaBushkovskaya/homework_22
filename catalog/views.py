from audioop import reverse

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.http import HttpResponse
from django.shortcuts import render

from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    """Контроллер для домашней страницы."""
    return render(request, "catalog/home.html")


class ContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        massage = request.POST.get('massage')
        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
