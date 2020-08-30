from django import forms
from . import models
# from bootstrap_modal_forms.forms import BSModalForm


class ItemForm(forms.ModelForm):

    class Meta:
        model = models.Item
        exclude = ['owner']

class ItemDraftForm(forms.ModelForm):

    class Meta:
        model = models.ItemDraft
        exclude = ['owner']