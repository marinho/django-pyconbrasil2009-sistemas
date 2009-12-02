# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

# Muda classe do AdminSite para classe customizada
from utils.admin import AdminSite
admin.site = AdminSite()

# Força os formatos de data para utilizar os definidos pelas settings
from utils.admin import force_date_formats #, AdminSite
force_date_formats()

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^doc/', include('django.contrib.admindocs.urls')),

    (r'^filtrar-empresas/$', 'sistema.views.filtrar_empresas'),
)

# Ajax FK Widget
urlpatterns += patterns('',
    (r'^ajax-fk/window/(?P<app>[\w_\.]+)/(?P<model>[\w_]+)/',
        'djangoplus.widgets.ajax_fk_widget.window_view', {},
        'ajax-fk-window-url'),
    (r'^ajax-fk/load/(?P<app>[\w_\.]+)/(?P<model>[\w_]+)/',
        'djangoplus.widgets.ajax_fk_widget.load_view', {},
        'ajax-fk-load-url'),
)

# Customizados
urlpatterns += patterns('',
    # Uncomment the next line to enable the admin:
    (r'', include(admin.site.urls)),
)

# URLS de arquivos estaticos, somente no ambiente em desenvolvimento
if settings.LOCAL:
    urlpatterns = patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    ) + urlpatterns

