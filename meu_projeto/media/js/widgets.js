// Validação para widgets comuns e simples

function valor_inteiro_on_change() {
    if ($(this).val() && !$(this).val().match(/^\d+$/)) {
        $(this).val('');
        alert('Valor numérico inteiro inválido!');
    }
}

function valor_inteiro_on_keypress() {
    if (e.which!=8 && e.which!=0 && (e.which<48 || e.which>57)){
        return false;
    }
}

function valor_decimal_on_change() {
    if ($(this).val() && !$(this).val().match(/^[\d,]+$/)) {
        $(this).val('');
        alert('Valor decimal inválido!');
    } else {
        //$(this).val(format_money(parseFloat($(this).val().replace(',', '.'))));
        $(this).val(format_money(converterParaFloat($(this).val())));
    }
}

function valor_decimal_on_keypress() {
    if (e.which!=8 && e.which!=0 && e.which!=44 && (e.which<48 || e.which>57)){
        return false;
    }
}

function carregar_cep_on_change() {
    if (!confirm('Deseja carregar o endereço do CEP informado?')) return

    var url = '/json/localizacao/carregar-cep/'+$(this).val()+'/';
    $.getJSON(url, function(json){
        if (json['res'] == RESULT_ERROR) {
            alert('CEP não encontrado na base de dados!');
        } else {
            $('#id_endereco').val(json['logradouro']);
            $('#id_complemento').val(json['complemento']);
            $('#id_bairro').val(json['bairro']);
            $('#id_cidade').val(json['cidade']);
            $('#id_cidade_display').text(json['cidade_nome']);
        }
    });
}

function show_popup(href) {
    if (href.indexOf('?') == -1) {
        href += '?_popup=1';
    } else {
        href  += '&_popup=1';
    }
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
}

$(document).ready(function(){
    // Inteiro
    $('.valor_inteiro').change(valor_inteiro_on_change).keypress(valor_inteiro_on_keypress);

    // Decimal
    $('.valor_decimal').change(valor_decimal_on_change).keypress(valor_decimal_on_keypress);

    // CEP
    $('.carregar_cep').change(carregar_cep_on_change);
});

