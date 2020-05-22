from django.contrib import admin
from .models import Item, ItemDraft, DraftFile, Review

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemDraft)
admin.site.register(DraftFile)
admin.site.register(Review)