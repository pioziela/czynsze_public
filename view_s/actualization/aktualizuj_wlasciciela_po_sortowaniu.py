from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import MieszkaniecForm
from create_pdf_documents.models import Mieszkaniec


@login_required
def aktualizuj_wlasciciela_po_sortowaniu(request, my_id, sorter):
    person = 2
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    form = MieszkaniecForm(request.POST or None, request.FILES or None, instance=wlasciciel)
    wlasciciel.pk = None
    if form.is_valid():
        form.save()
        return redirect(f'/wlasciciele/order/{sorter}/')
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person': person})