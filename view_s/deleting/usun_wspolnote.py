from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Wspolnota
from view_s.wszystkie_wspolnoty import wszystkie_wspolnoty


@login_required
def usun_wspolnote(request, my_id):
    wspolnota = get_object_or_404(Wspolnota, pk=my_id)
    if request.method == "POST":
        wspolnota.delete()
        return redirect(wszystkie_wspolnoty)
    return render(request, 'usun_wspolnote.html', {'wspolnota': wspolnota})