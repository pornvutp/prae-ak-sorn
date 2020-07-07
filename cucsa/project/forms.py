from django import forms
from . import models
from bootstrap_modal_forms.forms import BSModalForm


class ProjectForm(BSModalForm):
    
    class Meta:
        model = models.Project
        exclude = ['owner']