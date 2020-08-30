from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from django.shortcuts import get_object_or_404
from project.models import Project, ItemTag, TypeDimension

# from bootstrap_modal_forms.generic import BSModalCreateView

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class ItemDetail(generic.DetailView):
    model = models.Item


class ItemCreate(generic.CreateView):

    form_class = forms.ItemForm
    # fields = '__all__'
    model = models.Item

    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          project_id=self.request.GET.get('project_id')
          return reverse_lazy('project:detail', kwargs={'pk': project_id})

    def get_initial(self):
        project = get_object_or_404(Project, id=self.request.GET.get('project_id'))
        return {
            'project':project,
        }
    
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class DraftCreate(generic.CreateView):

    form_class = forms.ItemDraftForm
    # fields = '__all__'
    model = models.ItemDraft

    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          project_id=self.kwargs.get('pk')
          return reverse_lazy('item:detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_initial(self):
        item = get_object_or_404(models.Item, id=self.kwargs.get('pk'))
        return {
            'item':item,
        }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)
