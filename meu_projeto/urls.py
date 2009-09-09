# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Funções de Admin customizado
from utils.admin import force_date_formats #, AdminSite

# Muda classe do AdminSite para classe customizada
#admin.site = AdminSite()

# Força os formatos de data para utilizar os definidos pelas settings
force_date_formats()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^doc/', include('django.contrib.admindocs.urls')),
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

