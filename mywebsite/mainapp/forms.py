from django import forms
# from django.forms.fields import IntegerField
from django.core.exceptions import ValidationError

class SearchForm(forms.Form):
    # product_name = forms.CharField(max_length=200)
    price_min = forms.IntegerField()
    price_max = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        price_min = cleaned_data.get('price_min')
        price_max = cleaned_data.get('price_max')

        if(price_min > price_max):
            raise ValidationError(
                "Tidak boleh price minimum diatas price maksimum")