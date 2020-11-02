from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import MieszkaniecForm
from create_pdf_documents.models import Mieszkaniec
from view_s.wlasciciele import wlasciciele


@login_required
def aktualizacja_wlasciciela(request, my_id):
    person = 2
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    form = MieszkaniecForm(request.POST or None, request.FILES or None, instance=wlasciciel)
    wlasciciel.pk = None
    if form.is_valid():
        form.save()
        return redirect(wlasciciele)
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person': person, 'wlasciciel': wlasciciel})