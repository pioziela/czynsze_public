from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import Naliczenie_jeden_mieszkaniecForm


@login_required
def nowe_naliczenie_wlasciciela_po_wyborze(request, wybieracz):
    new = 0
    form = Naliczenie_jeden_mieszkaniecForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(f'/naliczenia/wlascicieli/select/{wybieracz}/')
    return render(request, 'naliczenie_wlasciciel_formularz.html', {'form': form, 'new': new})