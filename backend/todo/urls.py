from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_task),
    path('show/', views.get_all_tasks),
    path('delete/', views.delete_task),
    path('update/', views.update_task),
]