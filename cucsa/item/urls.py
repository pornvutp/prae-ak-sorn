from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'item'

urlpatterns = [
    # path('', views.ProjectPage.as_view(), name="home"),
    path("detail/<int:pk>/",views.ItemDetail.as_view(),name="detail"),

]