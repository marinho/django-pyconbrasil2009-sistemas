# -*- coding: utf-8 -*-
from django.contrib.localflavor.br.forms import BRCNPJField, BRCPFField
from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings

class CNPJField(BRCNPJField):
    def __init__(self, *args, **kwargs):
        super(CNPJField, self).__init__(*args, **kwargs)

        self.widget.attrs['class'] = self.widget.attrs.get('class', '') + ' cnpj mascara_cnpj'

class CPFField(BRCPFField):
    def __init__(self, *args, **kwargs):
        super(CPFField, self).__init__(*args, **kwargs)

        self.widget.attrs['class'] = self.widget.attrs.get('class', '') + ' cpf mascara_cpf'

class IntegerInput(forms.TextInput):
    class Media:
        js = (settings.MEDIA_URL+'js/widgets.js',)

    def render(self, name, value, attrs=None):
        u"""Acrescenta classe CSS para bloquear teclas que não sejam números"""
        attrs['class'] = ' '.join([attrs.get('class', ''), 'valor_inteiro'])

        return super(IntegerInput, self).render(name, value, attrs)

