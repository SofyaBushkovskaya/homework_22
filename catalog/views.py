from django.http import HttpResponse
from django.shortcuts import render


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
