from django.urls import path
from .views import contrat_detail, ContratListView

app_name = 'contrat'

urlpatterns = [
    path('', ContratListView.as_view(), name='contrat_list'),
    path('<int:pk>/', contrat_detail, name='contrat_detail'),
]