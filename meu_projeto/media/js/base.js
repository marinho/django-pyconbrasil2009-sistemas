// Funções automatizadas genéricas que executam ao carregar a página
$(document).ready(function(){
    // Move todos os botões adicionais para object-tools para a lista certa
    $('li.object-tools-button-begin').prependTo($('ul.object-tools'));
    $('li.object-tools-button-end').appendTo($('ul.object-tools'));

    // Move todos os botões adicionais de ação para o rodapé
    $('.footer-button').insertAfter($('.submit-row').find('.deletelink-box'));

    // Determina evento de seleção dos filtros laterais do admin
    $('select.admin_filter').change(function(){
        window.location = $(this).val();
    });

    // Desabilita tecla ENTER nos campos de input
    $('input:not([type=submit], [type=reset], [type=button], [type=image], .no_disable_return, #searchbar)').keypress(function(e){
        if (e.which == 13) {
            return false;
        }
    });
})
