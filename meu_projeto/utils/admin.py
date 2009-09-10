# -*- coding: utf-8 -*-
from django.contrib.admin.options import ModelAdmin as OriginalModelAdmin,\
        TabularInline as OriginalTabularInline
from django.contrib.admin.sites import AdminSite as OriginalAdminSite
from django.conf import settings
from django.db.models.fields import FieldDoesNotExist
from django.db import models
from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget

from djangoplus.templatetags.djangoplus_tags import moneyformat
from djangoplus.widgets.ajax_fk_widget import AjaxFKWidget

from currency_fields import CurrencyField, CurrencyInput
from datetime_fields import DateWidget, DATE_INPUT_FORMAT
from widgets import IntegerInput

class AdminSite(OriginalAdminSite):
    u"""Classe para sobrepor o site do Admin, para customizar o Admin"""

    def index(self, request, extra_context=None):
        request.user.message_set.create(message=u'Olá %s, seja bem-vindo!'%(
            request.user.get_full_name() or request.user.username,
            ))
        return super(AdminSite, self).index(request, extra_context=extra_context)

class ModelAdmin(OriginalModelAdmin):
    u"""Classe para customizar campos. Todas classes ModelAdmin do sistema
    devem herdar desta"""

    def __init__(self, *args, **kwargs):
        super(ModelAdmin, self).__init__(*args, **kwargs)
        
        list_display = []

        # Percorre todos os campos. Aqueles que são DecimalField passam a ser
        # encapsulados por um método que efetua a formatação. A ordenação e o
        # rótulo do campo são preservados
        for f in self.list_display:
            try:
                field = self.model._meta.get_field_by_name(f)[0]
                
                if isinstance(field, models.DecimalField):
                    func = eval('lambda self: moneyformat(self.%s)'%f)

                    # Preserva rótulo
                    func.short_description = field.verbose_name

                    # Preserva ordenação pelo campo original
                    func.admin_order_field = field.name

                    # Cria método que usa a função de encapsulamento
                    f = 'get_formatted_'+f
                    setattr(self.model, f, func)
            except FieldDoesNotExist:
                pass
            
            list_display.append(f)

        self.list_display = list_display

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModelAdmin, self).get_form(request, obj=None, **kwargs)

        # Define campos e seus novos tipos e widgets para a realidade brasileira
        change_form_fields(form)

        return form

class TabularInline(OriginalTabularInline):
    u"""Classe para customizar campos para master/detalhes. Todas classes
    TabularInline do sistema devem herdar desta"""

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(TabularInline, self).get_formset(request, obj=None, **kwargs)

        # Define campos e seus novos tipos e widgets para a realidade brasileira
        change_form_fields(formset.form)

        return formset

def change_form_fields(form):
    if not hasattr(form, 'base_fields'):
        return form

    # Muda comportamento de alguns tipos de campo
    for field_name, field in form.base_fields.items():
        # Campos monetários
        if isinstance(field, forms.DecimalField) or isinstance(field, forms.FloatField):
            new_field = CurrencyField()
            new_field.widget = CurrencyInput()

            new_field.required = form.base_fields[field_name].required
            new_field.initial = form.base_fields[field_name].initial
            new_field.label = form.base_fields[field_name].label

            form.base_fields[field_name] = new_field

        # Campos de data
        elif isinstance(field, forms.DateField):
            field.input_formats = (DATE_INPUT_FORMAT,)
            field.widget = DateWidget()

        # Widget de chave estrangeira informado manualmente
        elif isinstance(field.widget, ForeignKeyRawIdWidget):
            # Determina se o campo deve ser completado por zeros à esquerda
            # automaticamente ao usuário sair do campo
            db_field = form._meta.model._meta.get_field_by_name(field_name)[0]
            rel_field = db_field.rel.get_related_field()
            fill_left_zeros = isinstance(rel_field, models.CharField) and\
                    rel_field.max_length or 0

            widget_class = AjaxFKWidget

            field.widget = widget_class(
                    rel=db_field.rel, fill_left_zeros=fill_left_zeros,
                    )

        # Campos de números inteiros
        elif isinstance(field, forms.IntegerField):
            field.widget = IntegerInput()

        # Força caixa-alta (maiúsculas) na digitação
        if isinstance(field, forms.CharField) and not isinstance(field, (forms.EmailField, forms.URLField)):
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' forca_caixa_alta'

    return form

# Força os formatos de data para utilizar os definidos pelas settings
def force_date_formats():
    from django.utils import translation
    translation.get_date_formats = lambda: (settings.DATE_FORMAT, settings.DATETIME_FORMAT, settings.TIME_FORMAT)

