from django.db import models


class Blog(models.Model):
    objects = None
    name = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите заголовок"
    )

    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое продукта",
        null=False,
    )

    image = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Изображение",
        help_text="Добавьте изображение продукта",
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    sign_publication = models.BooleanField(
        default=True
    )

    view_count = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        default=0,
    )
