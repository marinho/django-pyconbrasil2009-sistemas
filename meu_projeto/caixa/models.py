# -*- coding: utf-8 -*-
import datetime

from django.db import models

from sistema.models import MultiEmpresa

class TipoComposicao(models.Model):
    class Meta:
        verbose_name = u'Tipo de Composição'
        verbose_name_plural = u'Tipos de Composição'

    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

TIPO_OPERACAO_CREDITO = 'c'
TIPO_OPERACAO_DEBITO = 'd'
TIPO_OPERACAO_CHOICES = (
    (TIPO_OPERACAO_CREDITO, u'Crédito'),
    (TIPO_OPERACAO_DEBITO, u'Débito'),
)

class LancamentoCaixa(MultiEmpresa):
    u"""Exemplo de classe de modelo com valor numérico, decimal e data. Também
    é exemplo de classe multi-empresa"""

    class Meta:
        verbose_name = u'Lançamento de Caixa'
        verbose_name_plural = u'Lançamentos de Caixa'
        permissions = (
            ('pode_fechar_caixa', 'Pode Fechar Caixa'),
        )

    data = models.DateField(blank=True, default=datetime.date.today)
    numero_documento = models.IntegerField(
            null=True,
            blank=True,
            db_index=True,
            verbose_name=u'Número de Documento',
            )
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_operacao = models.CharField(
            max_length=1,
            choices=TIPO_OPERACAO_CHOICES,
            db_index=True,
            verbose_name=u'Tipo de Operação',
            )
    observacao = models.TextField(blank=True, verbose_name=u'Observação')

class LancamentoCaixaComposicao(models.Model):
    u"""Um lançamento de caixa pode ser composto por valores em tipos de
    documentos diferentes, como dinheiro, cheque, vale, etc."""

    class Meta:
        verbose_name = u'Composição de Lançamento de Caixa'
        verbose_name_plural = u'Composições de Lançamento de Caixa'

    lancamento = models.ForeignKey(LancamentoCaixa)
    tipo_composicao = models.ForeignKey(TipoComposicao)
    valor = models.DecimalField(max_digits=12, decimal_places=2)


