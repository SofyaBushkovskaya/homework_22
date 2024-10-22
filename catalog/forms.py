from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта',
        })


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name.lower() in ["казино", "криптовалюта", "крипта", "биржа", "дешево",
                            "бесплатно", "обман", "полиция", "радар"]:
            self.add_error('name', 'Запрещённое слово.')

        if description.lower() in ["казино", "криптовалюта", "крипта", "биржа", "дешево",
                            "бесплатно", "обман", "полиция", "радар"]:
            self.add_error('description', 'Запрещённое слово.')


    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price < 0:
            raise forms.ValidationError("Стоимость продукта не может быть отрицательной.")

        if price == 0:
            raise forms.ValidationError("Стоимость продукта должна быть указана.")

        return price

    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')

        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")

        if not image.name.endswith(("jpeg", "jpg", "png")):
            raise forms.ValidationError("Формат файла не соответствует требованиям. "
                                        "Формат файла должен быть *.jpg, *.jpeg, *.png")
        return image
