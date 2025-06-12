from django.urls import path
from .views import maison_list, maison_detail

app_name = 'maison'

urlpatterns = [
    path('liste/', maison_list, name='maisons_list'),
    path('detail/<int:pk>/', maison_detail, name='maison_detail'),
]