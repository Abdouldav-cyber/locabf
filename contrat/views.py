from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Contrat

@login_required
def contrat_detail(request, pk):
    contrat = Contrat.objects.get(pk=pk)
    return render(request, 'contrat/contrat_detail.html', {'contrat': contrat})

class ContratListView(ListView):
    model = Contrat
    template_name = 'contrat/contrat_list.html'
    context_object_name = 'contrats'
    paginate_by = 10

    def get_queryset(self):
        return Contrat.objects.all().order_by('-date_signature')