from django.contrib.auth.decorators import login_required
from create_pdf_documents.forms import Naliczenie_jeden_mieszkaniecForm
from django.shortcuts import redirect, render
from view_s.wszystkie_naliczenia_wlascicieli import wszystkie_naliczenia_wlascicieli


@login_required
def nowe_naliczenie_wlasciciela(request):
    new = 0
    form = Naliczenie_jeden_mieszkaniecForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_naliczenia_wlascicieli)
    return render(request, 'naliczenie_wlasciciel_formularz.html', {'form': form, 'new': new})