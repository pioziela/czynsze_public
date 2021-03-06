from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import WyborForm, Sortowanie_naliczen_wlascicieliForm
from create_pdf_documents.models import Naliczenie_jeden_mieszkaniec, Wspolnota


@login_required
def sortowanie_naliczen_wlascicieli_po_wyborze(request, wybieracz, sorter):
    form = Sortowanie_naliczen_wlascicieliForm(request.POST or None)
    form2= WyborForm(request.POST or None)
    sort = form['parametry_sortowania_wlascicieli'].value()
    wybor2 = form2['wybor_wspolnoty'].value()
    element_sortujacy = sorter
    wybor = wybieracz
    adres = f'/nowe_naliczenie_wlasciciela/{wybor}/{element_sortujacy}/'
    adres2 = f'/edytuj_naliczenie_wlasciciela'
    adres3 = f'{wybor}'
    adres4 = f'/kopiuj_naliczenie_wlasciciela'
    lenght = 1
    wspolnota = Wspolnota.objects.get(id=wybieracz)
    if form.is_valid():
        return redirect(f'/naliczenia/wlascicieli/select/{wybor}/order/{sort}')
    if form2.is_valid():
        return redirect(f'/naliczenia/wlascicieli/select/{wybor2}')
    if element_sortujacy == 'data_utworzenia':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-data_utworzenia', '-data_dokumentu', 'wspolnota__wspolnota')
        sortowacz = 'data utworzenia'
    elif element_sortujacy == 'data_dokumentu':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-data_dokumentu', '-data_utworzenia',
                                                                'wspolnota__wspolnota')
        sortowacz = 'data dokumentu'
    elif element_sortujacy == 'wspolnota':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('wspolnota__wspolnota', '-data_dokumentu', '-data_utworzenia')
        sortowacz = 'wspólnota'
    elif element_sortujacy == 'data_obowiazywania_oplat':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-data_obowiazywania_oplat','-data_utworzenia', '-data_dokumentu', 'wspolnota__wspolnota')
        sortowacz = 'data obowiązywania opłat'
    elif element_sortujacy == 'stawka_zaliczka_eksploatacyjna':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_zaliczka_eksploatacyjna', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka zaliczka eksploatacyjna'
    elif element_sortujacy == 'stawka_podgrzanie_wody':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_podgrzanie_wody', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka podgrzanie wody'
    elif element_sortujacy == 'stawka_odprowadzenie_sciekow':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_odprowadzenie_sciekow', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka odprowadzenie ścieków'
    elif element_sortujacy == 'stawka_wywoz_nieczystosci':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_wywoz_nieczystosci', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka wywóz nieczystości'
    elif element_sortujacy == 'stawka_winda':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_winda', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka winda'
    elif element_sortujacy == 'stawka_fundusz_remontowy':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_fundusz_remontowy', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka fundusz remontowy'
    elif element_sortujacy == 'stawka_zimna_woda':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('-stawka_zimna_woda', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'stawka zimna woda'
    elif element_sortujacy == 'wlasciciel':
        sortowanie = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor).order_by('wlasciciel', '-data_dokumentu', '-data_utworzenia', 'wspolnota__wspolnota')
        sortowacz = 'właściciel'
    return render(request, 'sortowanie_naliczen_wlascicieli.html', {'sortowanie': sortowanie, 'form': form, 'form2': form2, 'lenght': lenght, 'sortowacz': sortowacz, 'wspolnota': wspolnota, 'adres': adres, 'adres2': adres2, 'adres3': adres3, 'adres4':adres4, 'wybor': wybor, 'element_sortujacy': element_sortujacy})