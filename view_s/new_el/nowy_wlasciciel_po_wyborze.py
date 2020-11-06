from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import MieszkaniecForm


@login_required
def nowy_wlasciciel_po_wyborze(request, wybieracz, where):
    person = 0
    form = MieszkaniecForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        if where == 'select':
            return redirect(f'/wlasciciele/select/{wybieracz}/')
        elif where == 'wszyscy':
            return redirect(f'/wspolnota/{wybieracz}/')
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person': person})