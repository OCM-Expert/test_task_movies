from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('diagram/', views.get_diagram_data, name='diagram'),
]