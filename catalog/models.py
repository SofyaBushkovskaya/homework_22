from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название", unique=True,
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Изображение",
        help_text="Добавьте изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="catalog",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0.00,
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    updated_at = models.DateField(
        auto_now=True,
    )
    publication_status = models.BooleanField(
        default=False,
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
