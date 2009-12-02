#/usr/bin/env python
# -*- coding:UTF-8 -*-
import re

from django.core.exceptions import ValidationError

expressao_cnpj = re.compile(r'^[\d]{2}[.][\d]{3}[.][\d]{3}[/][\d]{4}[-][\d]{2}$')

# -------------------------------------------------
# http://www.pythonbrasil.com.br/moin.cgi/VerificadorDeCnpj

"""
Este módulo fornece uma classe wrapper para ser usada com números de
CNPJ(CGC), que além de oferecer um método simples de verificação, também
conta com métodos para comparação e conversão.


>>> a = CNPJ('11222333000181')
>>> b = CNPJ('11.222.333/0001-81')
>>> c = CNPJ([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 8, 2])
>>> assert a.valido()
>>> assert b.valido()
>>> assert not c.valido()
>>> assert a == b
>>> assert not b == c
>>> assert not a == c
>>> assert eval(repr(a)) == a
>>> assert eval(repr(b)) == b
>>> assert eval(repr(c)) == c
>>> assert str(a) == \"11.222.333/0001-81\"
>>> assert str(b) == str(a)
>>> assert str(c) == \"11.222.333/0001-82\"
"""


class CNPJ(object):

    def __init__(self, cnpj):
        """Classe representando um número de CNPJ

        >>> a = CNPJ('11222333000181')
        >>> b = CNPJ('11.222.333/0001-81')
        >>> c = CNPJ([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 8, 2])

        """
        try:
            basestring
        except:
            basestring = (str, unicode)

        if isinstance(cnpj, basestring):
            if not cnpj.isdigit():
                cnpj = cnpj.replace(".", "")
                cnpj = cnpj.replace("-", "")
                cnpj = cnpj.replace("/", "")

            if not cnpj.isdigit:
                raise ValidationError("Valor não segue a forma xx.xxx.xxx/xxxx-xx")

        if len(cnpj) < 14:
            raise ValidationError("O número de CNPJ deve ter 14 digítos")

        self.cnpj = map(int, cnpj)


    def __getitem__(self, index):
        """Retorna o dígito em index como string

        >>> a = CNPJ('11222333000181')
        >>> a[9] == '0'
        True
        >>> a[10] == '0'
        True
        >>> a[9] == 0
        False
        >>> a[10] == 0
        False

        """
        return str(self.cnpj[index])

    def __repr__(self):
        """Retorna uma representação 'real', ou seja:

        eval(repr(cnpj)) == cnpj

        >>> a = CNPJ('11222333000181')
        >>> print repr(a)
        CNPJ('11222333000181')
        >>> eval(repr(a)) == a
        True

        """
        return "CNPJ('%s')" % ''.join([str(x) for x in self.cnpj])

    def __eq__(self, other):
        """Provê teste de igualdade para números de CNPJ

        >>> a = CNPJ('11222333000181')
        >>> b = CNPJ('11.222.333/0001-81')
        >>> c = CNPJ([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 8, 2])
        >>> a == b
        True
        >>> a != c
        True
        >>> b != c
        True

        """
        if isinstance(other, CNPJ):
            return self.cnpj == other.cnpj
        return False

    def __str__(self):
        """Retorna uma string do CNPJ na forma com pontos e traço

        >>> a = CNPJ('11222333000181')
        >>> str(a)
        '11.222.333/0001-81'

        """
        d = ((2, "."), (6, "."), (10, "/"), (15, "-"))
        s = map(str, self.cnpj)
        for i, v in d:
            s.insert(i, v)
        r = ''.join(s)
        return r

    def valido(self):
        """Valida o número de cnpj

        >>> a = CNPJ('11.222.333/0001-81')
        >>> a.valido()
        True
        >>> b = CNPJ('11222333000182')
        >>> b.valido()
        False

        """
        cnpj = self.cnpj[:12]
        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        # pegamos apenas os 9 primeiros dígitos do CNPJ e geramos os
        # dois dígitos que faltam
        while len(cnpj) < 14:

            r = sum([x*y for (x, y) in zip(cnpj, prod)])%11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            cnpj.append(f)
            prod.insert(0, 6)

        # se o número com os digítos faltantes coincidir com o número
        # original, então ele é válido
        return bool(cnpj == self.cnpj)

if __name__ == "__main__":
    import doctest, sys
    doctest.testmod(sys.modules[__name__])

