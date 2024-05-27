from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_task),
    path('show/', views.get_all_tasks),
    path('delete/<str:item_id>/', views.delete_task),
    path('update/<str:item_id>/', views.update_task),
]