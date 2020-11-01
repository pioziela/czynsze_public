from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import MieszkaniecForm


@login_required
def nowy_wlasciciel_szukanie_po_wyborze(request, wybieracz, szukacz):
    person = 0
    form = MieszkaniecForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(f'/wlasciciele/select/{wybieracz}/')
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person': person})