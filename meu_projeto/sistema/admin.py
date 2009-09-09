from django.contrib import admin

from djangoplus.widgets.ajax_fk_widget import AjaxFKWidget, AjaxFKDriver

from utils.admin import ModelAdmin

from models import Empresa

class AdminEmpresa(ModelAdmin):
    pass

class ModelAdminMultiEmpresa(ModelAdmin):
    pass

admin.site.register(Empresa, AdminEmpresa)

# Ajax FK Drivers

class AjaxEmpresa(AjaxFKDriver):
    model = Empresa
    list_display = ('id','nome')
    search_fields = ('id','nome')
    ordering = ('nome',)
AjaxFKWidget.register(AjaxEmpresa)

