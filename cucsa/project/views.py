from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse_lazy
# from bootstrap_modal_forms.generic import BSModalCreateView

from django.contrib.auth import get_user_model
User = get_user_model()

#from braces.views import SelectRelatedMixin

# from . import forms
from . import models
from . import forms

# Create your views here.

class ProjectPage(generic.ListView):
    model = models.Project
    # select_related = ("user", "group")

class ProjectCreate(generic.CreateView):

    form_class = forms.ProjectForm
    # fields = '__all__'
    model = models.Project
    
    # success_message = 'Success: Book was created.'
    success_url = reverse_lazy('project:home')
    

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"owner": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class ProjectDetail(generic.DetailView):
    model = models.Project
    # select_related = ("user", "group")

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(
    #         user__username__iexact=self.kwargs.get("username")
    #     )

