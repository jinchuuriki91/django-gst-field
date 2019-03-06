# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

# Project imports
from gst_field.constants import GSTIN_MAX_LENGTH, PAN_MAX_LENGTH
from gst_field import formfields


class GSTField(CharField):

    description = _("Goods and Services Tax")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", GSTIN_MAX_LENGTH)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': formfields.GSTField,
            **kwargs
        })


class PANField(CharField):

    description = _("Permanent account number")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", PAN_MAX_LENGTH)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': formfields.PANField,
            **kwargs
        })
