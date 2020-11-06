from django.contrib.auth.decorators import login_required
from create_pdf_documents.forms import Naliczenie_cala_wspolnotaForm
from django.shortcuts import redirect, render
from view_s.wszystkie_naliczenia_wspolnot import wszystkie_naliczenia_wspolnot


@login_required
def nowe_naliczenie_wspolnota(request):
    new = 0
    form = Naliczenie_cala_wspolnotaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_naliczenia_wspolnot)
    return render(request, 'naliczenie_wspolnota_formularz.html', {'form': form, 'new': new})