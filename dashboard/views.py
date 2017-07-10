# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.views.generic.list import ListView
import json
from django import forms
# from dashboard.forms import Patient_form
from dashboard.models import Outpatient
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'Outpatient'
    def get_queryset(self):
        """Return the last five visit."""
        return Outpatient.objects.order_by('initial_visit')[:5]
