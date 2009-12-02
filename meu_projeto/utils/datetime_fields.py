# -*- coding: utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings

DATE_INPUT_FORMAT = getattr(settings, 'DATE_INPUT_FORMAT', '%d/%m/%Y')

class DateWidget(forms.DateTimeInput):
    format = DATE_INPUT_FORMAT
    #format = '%Y-%m-%d'
    
    class Media:
        js = (settings.MEDIA_URL + "js/date.format.js",
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.MEDIA_URL + "js/admin/DateTimeShortcuts.js")

    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs.update({
            'class': 'vDateField mascara_data',
            'size': '10'
            })
        super(DateWidget, self).__init__(attrs=attrs)

