from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название", unique=True,
    )
    description = models.TextField()

    def __str__(self):
        return self.name

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

    view_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
