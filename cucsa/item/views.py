from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse_lazy
from . import models
# from . import forms
# from bootstrap_modal_forms.generic import BSModalCreateView

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class ItemDetail(generic.DetailView):
    model = models.Item