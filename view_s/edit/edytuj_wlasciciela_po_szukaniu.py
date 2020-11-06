from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import MieszkaniecForm
from create_pdf_documents.models import Mieszkaniec


@login_required
def edytuj_wlasciciela_po_szukaniu(request, my_id, szukacz):
    person = 1
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    form = MieszkaniecForm(request.POST or None, request.FILES or None, instance=wlasciciel)
    if form.is_valid():
        form.save()
        return redirect(f'/wlasciciele/filter/{szukacz}/')
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person': person})