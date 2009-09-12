from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Sum, Count
from django.contrib.auth.decorators import permission_required

from models import LancamentoCaixaComposicao

@permission_required('caixa.pode_fechar_caixa')
def fechar_caixa(request):
    title = u'Fechamento de Caixa'

    composicao = LancamentoCaixaComposicao.objects.values(
            'tipo_composicao','tipo_composicao__nome',
            ).annotate(
                    valor=Sum('valor'),
                    quantidade=Count('tipo_composicao'),
                    )
    print composicao

    soma_valor = sum([comp['valor'] for comp in composicao])
    soma_quantidade = sum([comp['quantidade'] for comp in composicao])

    return render_to_response(
            'admin/caixa/lancamentocaixa/fechar_caixa.html',
            locals(),
            context_instance=RequestContext(request),
            )

