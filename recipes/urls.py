from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('create', views.recipe_create),
    path('<int:id>/', views.recipe_detail),
    path('<int:id>/edit', views.recipe_update),
    path('<int:id>/delete', views.recipe_delete),
]