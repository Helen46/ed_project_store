from django.forms import ModelForm
from django import forms
from catalog.models import Product, Version


forbidden_words = [
    "казино", "криптовалюта", "крипта", "биржа", "дешево",
    "бесплатно", "обман", "полиция", "радар"
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "slug")

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("В названии содержeтся запрещенное слово")

        return cleaned_data


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

