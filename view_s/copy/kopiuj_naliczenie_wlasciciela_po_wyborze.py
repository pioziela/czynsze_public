from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import Naliczenie_jeden_mieszkaniecForm
from create_pdf_documents.models import Naliczenie_jeden_mieszkaniec


@login_required
def kopiuj_naliczenie_wlasciciela_po_wyborze(request, my_id, wybieracz):
    new = 2
    naliczenie = get_object_or_404(Naliczenie_jeden_mieszkaniec, pk=my_id)
    form = Naliczenie_jeden_mieszkaniecForm(request.POST or None, request.FILES or None, instance=naliczenie)
    naliczenie.pk = None
    if form.is_valid():
        form.save()
        return redirect(f'/naliczenia/wlascicieli/select/{wybieracz}/')
    return render(request, 'naliczenie_wlasciciel_formularz.html', {'form': form, 'new': new, 'naliczenie': naliczenie})