# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import Sum, Count
from django.conf.urls.defaults import url, patterns
from django import forms
from django.forms.models import ModelChoiceField

from sistema.admin import ModelAdminMultiEmpresa
from utils.admin import ModelAdmin, TabularInline
from utils.read_only import ReadOnlyTextWidget

from sistema.models import Empresa
from models import LancamentoCaixa, TipoComposicao, LancamentoCaixaComposicao,\
        TIPO_OPERACAO_CREDITO, TIPO_OPERACAO_DEBITO

class InlineLancamentoCaixaComposicao(TabularInline):
    model = LancamentoCaixaComposicao

class FormLancamentoCaixa(forms.ModelForm):
    class Meta:
        model = LancamentoCaixa

    def __init__(self, *args, **kwargs):
        self.base_fields['data'].widget = ReadOnlyTextWidget()

        super(FormLancamentoCaixa, self).__init__(*args, **kwargs)

class FormTipoComposicao(forms.Form):
    tipo_composicao = ModelChoiceField(
            queryset=TipoComposicao.objects.all(),
            required=False,
            )

class AdminLancamentoCaixa(ModelAdminMultiEmpresa):
    list_display = ('id','empresa','data','valor','tipo_operacao','numero_documento')
    list_filter = ('empresa','data','tipo_operacao')
    inlines = [InlineLancamentoCaixaComposicao]
    raw_id_fields = ('empresa',)
    search_fields = ('numero_documento','observacao',)
    tipo_composicao = None
    form = FormLancamentoCaixa
    fieldsets = (
            (u'Observação', {
                'fields': ('observacao',),
                'classes': ('wide','direita_flutuante')}),
            (None, {
                'fields': ('empresa','data','numero_documento','valor',
                    'tipo_operacao'),
                'classes': ('wide','esquerda_limitado')}),
            )

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        # Calcula valores do sumário
        qs = self.queryset(request).order_by()
        extra_context['quantidade'] = qs.aggregate(quantidade=Count('id'))['quantidade']
        extra_context['valor_creditos'] = qs.filter(tipo_operacao=TIPO_OPERACAO_CREDITO).aggregate(valor=Sum('valor'))['valor'] or 0
        extra_context['valor_debitos'] = qs.filter(tipo_operacao=TIPO_OPERACAO_DEBITO).aggregate(valor=Sum('valor'))['valor'] or 0
        extra_context['valor_total'] = extra_context['valor_creditos'] - extra_context['valor_debitos']

        # Form de filtro por tipo de composição
        if 'tipo_composicao' in request.GET:
            extra_context['form_tipo_comp'] = FormTipoComposicao(request.GET)

            if extra_context['form_tipo_comp'].is_valid():
                self.tipo_composicao = extra_context['form_tipo_comp'].cleaned_data['tipo_composicao']

                temp_get = dict(request.GET)
                temp_get.pop('tipo_composicao', None)
                request.GET = temp_get
        else:
            extra_context['form_tipo_comp'] = FormTipoComposicao()
            self.tipo_composicao = None

        return super(AdminLancamentoCaixa, self).changelist_view(request, extra_context)

    def get_urls(self):
        urls = super(AdminLancamentoCaixa, self).get_urls()

        minhas_urls = patterns('caixa.views',
                url(r'^fechar/$', 'fechar_caixa', name='fechar_caixa'),
                url(r'^editar-muitos/$', 'editar_muitos', name='editar_muitos'),
                )

        return minhas_urls + urls

    def queryset(self, request):
        qs = super(AdminLancamentoCaixa, self).queryset(request)

        if self.tipo_composicao:
            qs = qs.extra(
                where=(
                    """(select count(*) from caixa_lancamentocaixacomposicao as lcc
                        where lcc.lancamento_id = caixa_lancamentocaixa.id
                          and lcc.tipo_composicao_id = %s) >= 1""",
                    ),
                params=(self.tipo_composicao.pk,),
                )

        return qs

class AdminTipoComposicao(ModelAdmin):
    list_display = ('nome',)

admin.site.register(LancamentoCaixa, AdminLancamentoCaixa)
admin.site.register(TipoComposicao, AdminTipoComposicao)

