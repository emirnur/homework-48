from django import forms
from django.forms import widgets
from webapp.models import PRODUCT_CATEGORY_CHOICES


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=True, label='Поиск')


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название', widget=widgets.TextInput(
        attrs={'placeholder': 'Название'}))
    description = forms.CharField(max_length=2000, required=False, label='Описание',
                                  widget=widgets.Textarea)
    category = forms.ChoiceField(choices=PRODUCT_CATEGORY_CHOICES, required=True, label='Категория')
    amount = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')
