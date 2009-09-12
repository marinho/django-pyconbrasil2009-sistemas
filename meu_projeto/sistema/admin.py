from django.contrib import admin

from djangoplus.widgets.ajax_fk_widget import AjaxFKWidget, AjaxFKDriver

from utils.admin import ModelAdmin

from models import Empresa

class AdminEmpresa(ModelAdmin):
    pass

class ModelAdminMultiEmpresa(ModelAdmin):
    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}

        extra_context['empresas'] = Empresa.objects.all()

        return super(ModelAdminMultiEmpresa, self).change_view(request, object_id, extra_context)

admin.site.register(Empresa, AdminEmpresa)

# Ajax FK Drivers

class AjaxEmpresa(AjaxFKDriver):
    model = Empresa
    list_display = ('id','nome')
    search_fields = ('id','nome')
    ordering = ('nome',)
AjaxFKWidget.register(AjaxEmpresa)

