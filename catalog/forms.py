from django.forms import ModelForm, BooleanField
from django import forms
from catalog.models import Product, Version


forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StileFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "slug", "owner")

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError("В названии содержeтся запрещенное слово")

        return cleaned_data


class ProductModeratorForm(StileFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category", "is_published")


class VersionForm(StileFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
