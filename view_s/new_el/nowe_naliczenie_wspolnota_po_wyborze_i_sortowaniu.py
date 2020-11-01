from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import Naliczenie_cala_wspolnotaForm


@login_required
def nowe_naliczenie_wspolnota_po_wyborze_i_sortowaniu(request, wybieracz, sorter):
    new = 0
    form = Naliczenie_cala_wspolnotaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(f'/naliczenia/wspolnoty/select/{wybieracz}/order/{sorter}')
    return render(request, 'naliczenie_wspolnota_formularz.html', {'form': form, 'new': new})