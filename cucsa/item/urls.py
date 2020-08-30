from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'item'

urlpatterns = [

    path("create/", views.ItemCreate.as_view(), name="create"),
    path("<int:pk>/create-draft/", views.DraftCreate.as_view(), name="create-draft"),
    path("detail/<int:pk>/",views.ItemDetail.as_view(),name="detail"),

]