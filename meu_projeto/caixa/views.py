from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Sum, Count
from django.contrib.auth.decorators import permission_required
from django.forms.models import modelformset_factory

from models import LancamentoCaixaComposicao, LancamentoCaixa

from sistema.models import Empresa

@permission_required('caixa.pode_fechar_caixa')
def fechar_caixa(request):
    title = u'Fechamento de Caixa'

    composicao = LancamentoCaixaComposicao.objects.values(
            'tipo_composicao','tipo_composicao__nome',
            ).annotate(
                    valor=Sum('valor'),
                    quantidade=Count('tipo_composicao'),
                    )

    soma_valor = sum([comp['valor'] for comp in composicao])
    soma_quantidade = sum([comp['quantidade'] for comp in composicao])

    try:
        lancamento = LancamentoCaixa.objects.latest('pk')
    except LancamentoCaixa.DoesNotExist:
        lancamento = None

    return render_to_response(
            'admin/caixa/lancamentocaixa/fechar_caixa.html',
            locals(),
            context_instance=RequestContext(request),
            )

def editar_muitos(request):
    title = "Exemplo de formset"

    MinhaFormSet = modelformset_factory(
            LancamentoCaixa,
            )

    if request.method == 'POST':
        formset = MinhaFormSet(request.POST)

        if formset.is_valid():
            formset.save()
    else:
        formset = MinhaFormSet()

    return render_to_response(
            'admin/caixa/lancamentocaixa/editar_muitos.html',
            locals(),
            context_instance=RequestContext(request),
            )

