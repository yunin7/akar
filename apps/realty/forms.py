# -*- coding: utf-8 -*-
from django import forms

from models import Town, Type


class SearchForm(forms.Form):
    type = forms.ChoiceField(label=u'Тип')
    town = forms.ChoiceField(label=u'Город')
    price_max__gte = forms.IntegerField(label=u'минимальная стоимость')
    price_min__lte = forms.IntegerField(label=u'максимальная стоимость')
    square_max__gte = forms.IntegerField(label=u'минимальная стоимость')
    square_min__lte = forms.IntegerField(label=u'максимальная стоимость')


    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['type'].choices = Type.choices()
        self.fields['town'].choices = Town.choices()

    def filter(self):
        result = {}
        for key, value in self.data.items():
            if key in self.fields.keys() and int(value or 0):
                result[str(key)] = int(value)
        
        return result
