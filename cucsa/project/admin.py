from django.contrib import admin
from .models import Project, Announcement, TypeDimension, ItemTag, RefColor


# Register your models here.
admin.site.register(Project)
admin.site.register(Announcement)
admin.site.register(TypeDimension)
admin.site.register(ItemTag)
admin.site.register(RefColor)
