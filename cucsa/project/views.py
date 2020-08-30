from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse_lazy
# from bootstrap_modal_forms.generic import BSModalCreateView
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
User = get_user_model()

#from braces.views import SelectRelatedMixin

from . import models
from . import forms
from item.models import Item

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



    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(ProjectDetail, self).get_context_data(**kwargs)
    #     self.request.session['current_project'] = self.model.pk
    #     return context

# class ItemCreate(generic.CreateView):

#     form_class = forms.ItemForm
#     # fields = '__all__'
#     model = Item

#     def get_initial(self):
#         project = get_object_or_404(models.Project, pk=1)
#         return {
#             'project':project,
#         }
    
#     # success_message = 'Success: Book was created.'
#     success_url = reverse_lazy('project:home')

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.owner = self.request.user
#         self.object.save()
#         return super().form_valid(form)