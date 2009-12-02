# -*- coding: utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings

class CurrencyField(forms.RegexField):
    def __init__(self, regex=r'^\d{1,10}(,\d{1,2})?$', *args, **kwargs):
        super(CurrencyField, self).__init__(regex, *args, **kwargs)

    def clean(self, value):
        u"""Troca vírgula por ponto após a validação"""
        value = super(CurrencyField, self).clean(value)

        if not value:
            return None

        return value.replace(',','.')

    def widget_attrs(self, widget):
        return {'class': 'valor_monetario'}

class CurrencyInput(forms.TextInput):
    class Media:
        js = (settings.MEDIA_URL+'js/widgets.js',)

    def render(self, name, value, attrs=None):
        u"""Troca vírgula por vazio e ponto por vírgula após a renderização"""
        attrs['class'] = ' '.join([attrs.get('class', ''), 'valor_decimal'])
        ret = super(CurrencyInput, self).render(name, value, attrs)

        ret = ret.replace('.',',')

        return mark_safe(ret)

