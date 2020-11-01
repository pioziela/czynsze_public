from django.urls import path
from create_pdf_documents.views import index, nowa_wspolnota, nowy_wlasciciel, nowe_naliczenie_wspolnota,\
    nowe_naliczenie_wlasciciela, load_wspolnoty, wszystkie_wspolnoty, wszyscy_wlasciciele, wlasciciele, \
    wszystkie_naliczenia_wspolnot, wszystkie_naliczenia_wlascicieli, naliczenia, sortowanie_wlascicieli, \
    sortowanie_naliczen_wspolnot, sortowanie_naliczen_wlascicieli, wyszukiwanie, wybor_wlascicicieli_wspolnoty, \
    wybor_naliczen_wspolnot, wybor_naliczen_wlascicieli, wyszukiwanie_wlascicieli_po_wyborze, \
    sortowanie_naliczen_wspolnot_po_wyborze, sortowanie_naliczen_wlascicieli_po_wyborze, sortowanie_wlascicieli_po_wyborze, \
    usun_naliczenie_wspolnoty, usun_naliczenie_wlasciciela, usun_wspolnote, usun_wlasciciela, \
    historia_wlasciciela, historia_wszyscy_wlasciciele, edytuj_wlasciciela, edytuj_wlasciciela_historia,\
    edytuj_wlasciciela_historia_wszyscy, edytuj_naliczenie_wlasciciela, edytuj_naliczenie_wlasciciela_po_wyborze,\
    edytuj_wspolnote, edytuj_naliczenie_wspolnoty_po_wyborze, edytuj_naliczenie_wspolnoty, edytuj_wlasciciela_szukanie_po_wyborze,\
    edytuj_wlasciciela_sortowanie_po_wyborze, edytuj_wlasciciela_po_wyborze, edytuj_wlasciciela_po_sortowaniu,\
    edytuj_wlasciciela_po_szukaniu

urlpatterns = [
    path('index/', index),
    path('naliczenia/', naliczenia),
    path('nowa_wspolnota/', nowa_wspolnota),
    path('nowy_wlasciciel/', nowy_wlasciciel),
    path('nowe_naliczenie_wspolnota/', nowe_naliczenie_wspolnota),
    path('nowe_naliczenie_wlasciciela/', nowe_naliczenie_wlasciciela),
    path('ajax/load_wspolnoty', load_wspolnoty, name='ajax_load_wspolnoty'),
    path('wspolnoty/', wszystkie_wspolnoty),
    path('wspolnota/<int:my_id>/', wszyscy_wlasciciele),
    path('wlasciciele/', wlasciciele),
    path('naliczenia_wspolnot/', wszystkie_naliczenia_wspolnot),
    path('naliczenia_mieszkaniec/', wszystkie_naliczenia_wlascicieli),
    path('wlasciciele/order/<sorter>/', sortowanie_wlascicieli),
    path('naliczenia/wspolnoty/order/<sorter>/', sortowanie_naliczen_wspolnot),
    path('naliczenia/wlascicieli/order/<sorter>/', sortowanie_naliczen_wlascicieli),
    path('wlasciciele/filter/<szukacz>/', wyszukiwanie),
    path('wlasciciele/select/<wybieracz>/', wybor_wlascicicieli_wspolnoty),
    path('naliczenia/wspolnota/select/<wybieracz>/', wybor_naliczen_wspolnot),
    path('naliczenia/wlascicieli/select/<wybieracz>/', wybor_naliczen_wlascicieli),
    path('wlasciciele/select/<wybieracz>/filter/<szukacz>', wyszukiwanie_wlascicieli_po_wyborze),
    path('naliczenia/wspolnoty/select/<wybieracz>/order/<sorter>', sortowanie_naliczen_wspolnot_po_wyborze),
    path('naliczenia/wlascicieli/select/<wybieracz>/order/<sorter>', sortowanie_naliczen_wlascicieli_po_wyborze),
    path('wlasciciele/select/<wybieracz>/order/<sorter>', sortowanie_wlascicieli_po_wyborze),
    path('usun_naliczenie_wspolnoty/<int:my_id>/', usun_naliczenie_wspolnoty),
    path('usun_naliczenie_wlasciciela/<int:my_id>/', usun_naliczenie_wlasciciela),
    path('usun_wspolnote/<int:my_id>/', usun_wspolnote),
    path('usun_wlasciciela/<int:my_id>/', usun_wlasciciela),
    path('historia_wlasciciela/<int:my_id>/', historia_wlasciciela),
    path('historia/wspolnota/<int:my_id>/', historia_wszyscy_wlasciciele),
    path('edytuj_wlasciciela/<int:my_id>/', edytuj_wlasciciela),
    path('edytuj_wlasciciela/historia/<int:my_id>/', edytuj_wlasciciela_historia),
    path('edytuj_wlasciciela/wszyscy/historia/<int:my_id>/', edytuj_wlasciciela_historia_wszyscy),
    path('edytuj_wlasciciela/<int:my_id>/select/<sorter>/', edytuj_wlasciciela_po_sortowaniu),
    path('edytuj_wlasciciela/<int:my_id>/filter/<szukacz>/', edytuj_wlasciciela_po_szukaniu),
    path('edytuj_wlasciciela/<int:my_id>/<wybieracz>/<where>/', edytuj_wlasciciela_po_wyborze),
    path('edytuj_wlasciciela/<int:my_id>/<wybieracz>/<where>/<sorter>/', edytuj_wlasciciela_sortowanie_po_wyborze),
    path('edytuj_wlasciciela/<int:my_id>/<wybieracz>/select/filter/<szukacz>/', edytuj_wlasciciela_szukanie_po_wyborze),
    path('edytuj_wspolnote/<int:my_id>/', edytuj_wspolnote),
    path('edytuj_naliczenie_wspolnoty/<int:my_id>/', edytuj_naliczenie_wspolnoty),
    path('edytuj_naliczenie_wspolnoty/<int:my_id>/<wybieracz>/', edytuj_naliczenie_wspolnoty_po_wyborze),
    path('edytuj_naliczenie_wlasciciela/<int:my_id>/', edytuj_naliczenie_wlasciciela),
    path('edytuj_naliczenie_wlasciciela/<int:my_id>/<wybieracz>/', edytuj_naliczenie_wlasciciela_po_wyborze),
]