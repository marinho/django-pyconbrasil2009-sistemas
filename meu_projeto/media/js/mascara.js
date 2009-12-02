/* Script responsável por definir classes CSS de máscaras e aplicar seus
 * respectivos comportamentos com JavaScript.
 *
 * Este script depende do plugin para jQuery "jquery.maskedinput.js",
 * disponível em:
 * - http://digitalbush.com/projects/masked-input-plugin/
 */

$(document).ready(function(){
    // CEP
    $('.mascara_cep').mask('99999-999');

    // CNPJ
    $('.mascara_cnpj').mask('99.999.999/9999-99');

    // CPF
    $('.mascara_cpf').mask('999.999.999-99');

    // Data
    $('.mascara_data').mask('99/99/9999');

    // Hora
    $('.mascara_hora').mask('99:99');

    // Telefone
    $('.mascara_telefone').mask('(99)9999-9999');
});
