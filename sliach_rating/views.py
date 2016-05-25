from django.contrib import messages
from django.core import validators
from django.core.urlresolvers import reverse
from django.db.models import Q, Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import models
from . import forms


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


def get_state(request, pk):
    state = models.State.objects.get(pk=pk)
    sluchim = models.Sluchim.objects.filter(state=state)
    return render(request,
                  'sliach_rating/sluchim_list.html', 
                  {'sluchim': sluchim})


def rating_create(request, sliach_pk):
    sliach = get_object_or_404(models.Sluchim, pk=sliach_pk)
    form = forms.RatingForm()

    if request.method == 'POST':
        form = forms.RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.sliach = sliach
            rating.save()
            messages.add_message(request, messages.SUCCESS, "Comment addded!")
            return HttpResponseRedirect(reverse('sluchim:list'))
    return render(
        request,
        'sliach_rating/rating_form.html',
        {'form': form, 'sliach': sliach}
    )
    