from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProjectPage(TemplateView):
    template_name = 'project/index.html'
