// Função para encontrar pai de um tipo X
function find_parent_with_tag(obj, tag_name) {
    if (obj.parent().attr('tagName').toLowerCase() == tag_name.toLowerCase()) {
        return obj.parent();
    } else if (!obj.parent().attr('tagName')) {
        return null;
    }

    return find_parent_with_tag(obj.parent(), tag_name);
}

// Função que arredonda com decimais
function round_number(num, dec) {
	var result = Math.round(num*Math.pow(10,dec))/Math.pow(10,dec);
	return result;
}

// Função para formatar valor monetário
function format_money(num) {
	var result = String(round_number(num, 2));

    if (result.indexOf('.') == -1) {
        result += ',00';
    } else if (result.indexOf('.') == result.length - 2) {
        result += '0';
    }
    
    return result.replace('.',',');
}

// Função que converte string para float
function converterParaFloat(val) {
    return parseFloat(val.replace('.','').replace(',','.'));
}

// Função que converte data em string (dd/mm/yyyy) para objeto Date
function converterParaData(str){
    var bits = str.split('/');
    return new Date(
            parseInt(bits[2]), // Ano
            parseInt(bits[1].charAt(0) == '0' ? bits[1].charAt(1) : bits[1]) - 1, // Mes (remove zero à esquerda)
            parseInt(bits[0].charAt(0) == '0' ? bits[0].charAt(1) : bits[0]) // Mes (remove zero à esquerda)
            );
}

// Função que incrementa dias ao um objeto Date
Date.prototype.incDays = function (days) {
    var second = 1000;
    var minute = second * 60;
    var hour = minute * 60;
    var day = hour * 24;
    var dayNumber = this.getTime();
    var ret = new Date();
    ret.setTime(dayNumber + day * days)

    return ret;
}

// Função que incrementa meses ao um objeto Date
Date.prototype.incMonths = function (months) {
    var day = this.getDate();
    var month = this.getMonth();
    var year = this.getFullYear();

    month += months;

    while (month > 11) {
        year++;
        month -= 12;
    }

    return new Date(year, month, day);
}

function getElementsByTagName(tagName, pai) {
    if (!pai) pai = document

    var ret = [];

    for (var i=0; i<pai.childNodes.length; i++) {
        if (pai.childNodes[i].tagName == tagName) {
            ret.push(pai.childNodes[i]);
        }
    }

    return ret;
}

if (TESTING) {
    $(document).ready(function() {
        // Testa find_parent_with_tag
        alert(find_parent_with_tag($('#id_empresa'), 'h1').length == 1)

        // Testa round_number
        alert(round_number(15.919,2) == 15.92)

        // Testa format_money
        alert(format_money(15.919) == '15,92')
        alert(format_money(15.91) == '15,91')
        alert(format_money(15.9) == '15,90')
        alert(format_money(15) == '15,00')
    });
}

