from django.contrib import messages
from django.db.models import Q, Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import models


def sluchim_list(request):
    sluchim = models.Sluchim.objects.all()
    return render(request,
                 'sliach_rating/sluchim_list.html',
                 {'sluchim': sluchim})


def sliach_details(request, pk):
    sliach = get_object_or_404(models.Sluchim, pk=pk)
    return render(request,
                  'sliach_rating/sliach_details.html',
                  {'sliach': sliach})


def search_state(request):
    search = request.GET.get('q')
    sluchim = models.Sluchim.objects.filter(state__state__icontains=search)
    return render(request,
                  'sliach_rating/sluchim_list.html', 
                  {'sluchim': sluchim})