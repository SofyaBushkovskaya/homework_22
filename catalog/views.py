from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.http import HttpResponse
from django.shortcuts import render

from catalog.forms import ProductForm, ProductModeratorForm
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")



