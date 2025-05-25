from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    path('notes_list/', views.notes_list, name='notes_list'),
]