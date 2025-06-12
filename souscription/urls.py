from django.urls import path
from .views import souscription_form, SouscriptionListView, SouscriptionDetailView

app_name = 'souscription'

urlpatterns = [
    path('form/<int:maison_id>/', souscription_form, name='souscription_form'),
    path('', SouscriptionListView.as_view(), name='souscription_list'),
    path('<int:pk>/', SouscriptionDetailView.as_view(), name='souscription_detail'),
]