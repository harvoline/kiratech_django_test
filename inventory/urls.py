from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:inventory_id>/', views.show, name='show'),
]