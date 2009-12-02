from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

class MultiEmpresa(models.Model):
    class Meta:
        abstract = True

    empresa = models.ForeignKey(Empresa)

