import calendar
from django.contrib.auth.decorators import login_required
from create_pdf_documents.models import Wspolnota, Mieszkaniec, Naliczenie_jeden_mieszkaniec
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DejaVuSans','DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold','DejaVuSans-Bold.ttf'))


@login_required
def pdf_mieszkaniec(request, my_id):
    response = HttpResponse(content_type='application/pdf')
    tytul_data = str(Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).data_dokumentu)
    tytul_mieszkaniec = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).wlasciciel
    id_wlasciciel = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).wlasciciel.id
    pdf_name = f'{str(tytul_mieszkaniec).replace(" ","")}_{tytul_data}.pdf'
    intab = "ąęółńśźż"
    outtab = "aeolnszz"
    trantab = str.maketrans(intab, outtab)
    pdf_new_name = pdf_name
    response['Content-Disposition'] = f'attachment; filename = {pdf_new_name.translate(trantab)}'
    p = canvas.Canvas(response, pagesize=A4)
    data = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).data_dokumentu
    data_poczatek_oplat = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).data_obowiazywania_oplat
    data_koniec_oplat = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).oplaty_do
    zmiana = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).zmianie_ulegaja_oplaty_za
    stawka_eksploatacja = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_zaliczka_eksploatacyjna
    stawka_CO_miernik = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_CO_miernik
    stawka_cw = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_podgrzanie_wody
    stawka_zw = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_zimna_woda
    stawka_scieki = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_odprowadzenie_sciekow
    stawka_nieczystosci = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_wywoz_nieczystosci
    stawka_winda = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_winda
    stawka_miejsce_postojowe_komorka = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_miejsce_postojowe_komorka
    stawka_fundusz_remontowy = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).stawka_fundusz_remontowy
    informacja = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).dodatkowa_informacja_gora
    informacja_dol = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).dodatkowa_informacja_dol
    informacja_dol_2 = Naliczenie_jeden_mieszkaniec.objects.get(id=my_id).dodatkowa_informacja_dol_2
    rok, miesiac = data_koniec_oplat.year, data_koniec_oplat.month
    ilosc_dni_w_miesiacu = calendar.monthrange(rok, miesiac)[1]
    rob = 1
    ilosc_dodanych_do_naliczenia_wlascicieli = 0
    licznik_braku_dodanych_wlascicieli = 0
    if data_koniec_oplat > data_poczatek_oplat:
        if data_poczatek_oplat.day == 1 and data_koniec_oplat.day == ilosc_dni_w_miesiacu:
            procent = 1
        elif data_poczatek_oplat.day == 1 and data_koniec_oplat.day < ilosc_dni_w_miesiacu and data_poczatek_oplat.month == data_koniec_oplat.month:
            ilosc_dni_oplat = data_koniec_oplat.day
            procent = ilosc_dni_oplat / ilosc_dni_w_miesiacu
        elif data_poczatek_oplat.day > 1 and data_koniec_oplat.day == ilosc_dni_w_miesiacu and data_poczatek_oplat.month == data_koniec_oplat.month:
            ilosc_dni_oplat = data_koniec_oplat.day - data_poczatek_oplat.day + 1
            procent = ilosc_dni_oplat / ilosc_dni_w_miesiacu
        elif data_poczatek_oplat.day > 1 and data_koniec_oplat.day < ilosc_dni_w_miesiacu and data_poczatek_oplat.month == data_koniec_oplat.month:
            ilosc_dni_oplat = data_koniec_oplat.day - data_poczatek_oplat.day + 1
            procent = ilosc_dni_oplat / ilosc_dni_w_miesiacu
        else:
            rob = 0
            licznik_braku_dodanych_wlascicieli = 1
            p.setFont("DejaVuSans-Bold", 14, leading=None)
            p.drawString(40, 720, f'BŁĄD:')
            p.drawString(40, 700, f'Gdy naliczenie obejmuje okres krótszy niż 1 miesiąc,')
            p.drawString(40, 680, f'to miesiąc początka i końca opłat powinny być takie same,')
            p.drawString(40, 660, f'a ustawiono jako różne.')
            p.setFont("DejaVuSans", 10, leading=None)
            p.drawString(40, 610, f'ZASADY USTAWIANIA DAT PRZY TWORZENIU NALICZEŃ:')
            p.drawString(50, 595, f'1.  Gdy okres obowiązywania naliczenia ma być dłuższy niż 1 miesiąc, to data')
            p.drawString(55, 580, f'rozpoczęcia opłat musi być ustawiona na pierwszy dzień miesiąca, a data końca')
            p.drawString(55, 565, f'opłat musi być ustawiona na ostatni dzień miesiąca - najlepiej dla jakiejś')
            p.drawString(55, 550, f'bardzo odległej daty.')
            p.drawString(50, 535, f'2.  Gdy wiadomo kiedy kończy się czas trwania naliczenia obejmującego okres')
            p.drawString(55, 520, f'większy niż jeden miesiąc, należy edytować formularz naliczenia i ustawić datę')
            p.drawString(55, 505, f'końca trwania naliczenia na właściwą')
            p.drawString(50, 490,
                         f'3.  Gdy naliczenie obejmuje okres krótszy niż 1 miesiąc, to miesiąć początka i końca')
            p.drawString(55, 475, f'opłat powinny być takie same.')
        if rob == 0:
            None
        else:
            n = 0
            ten_mieszkaniec = Mieszkaniec.objects.get(id=id_wlasciciel)
            if data_poczatek_oplat >= ten_mieszkaniec.aktywny_od and data_poczatek_oplat <= ten_mieszkaniec.aktywny_do \
                and data_poczatek_oplat >= ten_mieszkaniec.dane_od and data_poczatek_oplat <= ten_mieszkaniec.dane_do \
                and data_koniec_oplat <= ten_mieszkaniec.aktywny_do:
                    n = n + 1
                    ilosc_dodanych_do_naliczenia_wlascicieli = ilosc_dodanych_do_naliczenia_wlascicieli + 1
                    imie = ten_mieszkaniec.imie
                    nazwisko = ten_mieszkaniec.nazwisko
                    ulica = ten_mieszkaniec.adres_ulica
                    dom = ten_mieszkaniec.adres_numer_domu
                    mieszkanie = ten_mieszkaniec.adres_numer_mieszkania
                    wspolnota = ten_mieszkaniec.wspolnota
                    konto_eksp = Wspolnota.objects.get(wspolnota=wspolnota).konto_eksploatacyjne
                    konto_rem = Wspolnota.objects.get(wspolnota=wspolnota).konto_remontowe
                    powierzchnia = ten_mieszkaniec.powierzchnia_mieszkania
                    if stawka_CO_miernik == 0:
                        zaliczka_CO = ten_mieszkaniec.zaliczka_CO
                    else:
                        zaliczka_CO = ten_mieszkaniec.zaliczka_CO_miernik
                    zaliczka_cw = ten_mieszkaniec.podgrzanie_wody_objetosc
                    zaliczka_zw = ten_mieszkaniec.zimna_woda_objetosc
                    zaliczka_scieki = ten_mieszkaniec.odprowadzenie_sciekow_objetosc
                    osoby = ten_mieszkaniec.ilosc_osob
                    winda = ten_mieszkaniec.winda
                    zaliczka_uchyl_wody = ten_mieszkaniec.uchyl_wody
                    zaliczka_miejsce_postojowe_komorka = ten_mieszkaniec.miejsce_postojowe_komorka
                    p.setFont("DejaVuSans", 10, leading=None)
                    p.drawImage('static/images/logo_PNG_black.png', 40, 750, 230, 68)
                    p.drawImage('static/images/linia.png', 10, 730, 575)
                    p.setFont("DejaVuSans-Bold", 9, leading=None)
                    p.drawString(430, 810, 'Kontakt:')
                    p.setFont("DejaVuSans", 9, leading=None)
                    p.drawString(430, 797, 'ul. Bydgoska 94')
                    p.drawString(430, 784, '87-100 Toruń')
                    p.drawString(430, 771, 'tel. (56) 653 81 41')
                    p.drawString(430, 758, 'e-mail: romanzie@o2.pl')
                    p.drawString(430, 745, 'www.dolmar-ii.pl')
                    p.drawString(430, 700, f'Toruń, dnia {data} r.')
                    p.setFont("DejaVuSans-Bold", 10, leading=None)
                    p.drawString(300, 670, 'Sz.P.')
                    p.drawString(300, 657, f'{nazwisko} {imie}')
                    p.drawString(300, 644, f'ul. {ulica} {dom} m. {mieszkanie}')
                    p.drawString(300, 631, '87-100 Toruń')
                    p.setFont("DejaVuSans", 10, leading=None)
                    if informacja != 'brak':
                        p.drawString(40, 573, f'{informacja}:')
                    p.drawString(40, 560, f'Zarząd Wsp. Mieszk.')
                    dlugosc_wspolnoty = len(str(wspolnota))
                    if dlugosc_wspolnoty <= 10:
                        p.drawString(145+dlugosc_wspolnoty*7.5, 560, f'uprzejmie informuje o wysokości opłat obowiązujących')
                    elif 15 >= dlugosc_wspolnoty > 10:
                        p.drawString(145+dlugosc_wspolnoty*7, 560, f'uprzejmie informuje o wysokości opłat obowiązujących')
                    elif dlugosc_wspolnoty > 15:
                        p.drawString(145+dlugosc_wspolnoty*6.5, 560, f'uprzejmie informuje o wysokości opłat obowiązujących')
                    p.drawString(40, 547, f'od                          na utrzymanie nieruchomości wspólnej.')
                    if zmiana != 'nic':
                        p.drawString(336, 547, f'Zmianie ulegają opłaty zaliczkowe za:')
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        p.drawString(40, 534, f'{zmiana}.')
                    p.setFont("DejaVuSans-Bold", 10, leading=None)
                    p.drawString(145, 560, f'{wspolnota}')
                    p.drawString(55, 547, f'{data_poczatek_oplat} r.')
                    p.setFont("DejaVuSans", 10, leading=None)
                    p.drawImage('static/images/linia.png', 40, 465, 515, 1.5)
                    p.drawImage('static/images/linia.png', 40, 445, 515, 1.5)
                    p.drawImage('static/images/pole.png', 40, 446, 515, 19)
                    p.drawImage('static/images/pole.png', 456, 199, 99, 17)
                    p.setFont("DejaVuSans-Bold", 10, leading=None)
                    p.drawString(90, 452, 'zaliczka/świadczenie')
                    p.drawString(285, 452, 'stawka')
                    p.drawString(378, 452, 'podstawa')
                    p.drawString(485, 452, 'kwota')
                    p.drawImage('static/images/pole.png', 455, 266, 100, 17)
                    p.drawString(50, 270, 'MIESIĘCZNA NALEŻNOŚĆ NA POCZET FUNDUSZU EKSPLOATACYJNEGO:')
                    p.drawString(50, 203, 'MIESIĘCZNA NALEŻNOŚĆ NA POCZET FUNDUSZU REMONTOWEGO:')
                    p.drawImage('static/images/linia.png', 40, 427, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 409, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 391, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 373, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 355, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 337, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 319, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 301, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 283, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 265, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 234, 515, 1.5)
                    p.drawImage('static/images/linia.png', 40, 216, 515, 0.4)
                    p.drawImage('static/images/linia.png', 40, 198, 515, 0.4)
                    p.drawImage('static/images/linia2.png', 255, 216, 0.7, 18)
                    p.drawImage('static/images/linia2.png', 355, 216, 0.7, 18)
                    p.drawImage('static/images/linia2.png', 455, 198, 0.7, 36)
                    p.drawImage('static/images/linia2.png', 255, 283, 0.7, 182)
                    p.drawImage('static/images/linia2.png', 355, 283, 0.7, 182)
                    p.drawImage('static/images/linia2.png', 455, 265, 0.7, 200)
                    p.setFont("DejaVuSans-Bold", 13, leading=None)
                    p.drawString(200, 473, 'Fundusz eksploatacyjny')
                    p.drawString(215, 241, 'Fundusz remontowy')
                    p.setFont("DejaVuSans-Bold", 10, leading=None)
                    p.drawString(181, 164, f'do dnia 10 każdego miesiąca')
                    p.drawString(40, 151, f'{wspolnota}. Numery kont rachunków bankowych:')
                    p.drawString(170, 131, f'{konto_eksp}')
                    if konto_rem != 'brak':
                        p.drawString(170, 111, f'{konto_rem}')
                    p.setFont("DejaVuSans", 10, leading=None)
                    p.drawString(40, 164,
                                 f'Wpłaty prosimy dokonywać                                                     na konta bankowe Wspól. Mieszkaniowej')
                    p.drawString(40, 131, f'- konto eksploatacyjne:')
                    if konto_rem != 'brak':
                        p.drawString(40, 111, f'- konto remontowe:')
                    if informacja_dol != 'brak':
                        p.drawString(40, 84, f'{informacja_dol}')
                    if informacja_dol_2 != 'brak':
                        p.drawString(40, 71, f'{informacja_dol_2}')
                    if powierzchnia != 0:
                        p.drawString(377, 433, f'{powierzchnia:.2f} [m2]')
                    else:
                        p.drawString(390, 433, f'------')
                    p.drawString(89, 433, 'zaliczka eksploatacyjna')
                    p.drawString(94, 415, 'centralne ogrzewanie')
                    p.drawString(105, 397, 'podgrzanie wody')
                    p.drawString(116, 307, 'uchył wody')
                    if zaliczka_uchyl_wody != 0:
                        p.drawString(380, 307, f'{zaliczka_uchyl_wody:.2f} [m3]')
                    else:
                        p.drawString(390, 307, f'------')
                    p.drawString(116, 379, 'zimna woda')
                    p.drawString(89, 289, 'miejsce postojowe/komórka')
                    if zaliczka_miejsce_postojowe_komorka != 0:
                        p.drawString(380, 289, f'{zaliczka_miejsce_postojowe_komorka:.2f} [m2]')
                    else:
                        p.drawString(390, 289, f'------')
                    if zaliczka_cw != 0:
                        p.drawString(380, 397, f'{zaliczka_cw:.2f} [m3]')
                    else:
                        p.drawString(390, 397, f'------')
                    p.drawString(116, 379, 'zimna woda')
                    if zaliczka_zw != 0:
                        p.drawString(380, 379, f'{zaliczka_zw:.2f} [m3]')
                    else:
                        p.drawString(390, 379, f'------')
                    p.drawString(88, 361, 'odprowadzenie ścieków')
                    if zaliczka_scieki != 0:
                        p.drawString(380, 361, f'{zaliczka_scieki:.2f} [m3]')
                    else:
                        p.drawString(390, 361, f'------')
                    p.drawString(79, 343, 'wywóz nieczystości stałych')
                    if osoby != 0:
                        p.drawString(386, 343, f'{osoby:.2f} os.')
                    else:
                        p.drawString(390, 343, f'------')
                    p.drawString(100, 325, 'zaliczka na windę')
                    if winda != 0:
                        p.drawString(386, 325, f'{winda:.2f} os.')
                    else:
                        p.drawString(390, 325, f'------')
                    p.drawString(79, 222, 'zaliczka fundusz remontowy')
                    if powierzchnia != 0:
                        p.drawString(377, 222, f'{powierzchnia:.2f} [m2]')
                    else:
                        p.drawString(390, 222, f'------')
                    if procent == 1:
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        p.drawString(192, 510, f'{data_poczatek_oplat} r.')
                        p.setFont("DejaVuSans", 10, leading=None)
                        p.drawString(150, 510, f'Od dnia                          miesięczne należności wynoszą:')
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        if stawka_fundusz_remontowy != 0 or powierzchnia != 0:
                            p.drawString(480, 204, f'{stawka_fundusz_remontowy * powierzchnia:.2f} zł')
                        else:
                            p.drawString(480, 204, f'------')
                        p.setFont("DejaVuSans", 10, leading=None)
                        if stawka_eksploatacja != 0:
                            p.drawString(288, 433, f'{stawka_eksploatacja:.2f} zł')
                        else:
                            p.drawString(290, 433, f'------')
                        if stawka_CO_miernik != 0:
                            p.drawString(288, 415, f'{stawka_CO_miernik:.2f} zł')
                        if stawka_eksploatacja != 0 or powierzchnia != 0:
                            p.drawString(480, 433, f'{powierzchnia * stawka_eksploatacja:.2f} zł')
                        else:
                            p.drawString(480, 433, f'------')
                        if zaliczka_CO != 0:
                            if stawka_CO_miernik == 0:
                                p.drawString(382, 415, f'{zaliczka_CO:.2f} zł')
                                p.drawString(480, 415, f'{zaliczka_CO:.2f} zł')
                            else:
                                p.drawString(382, 415, f'{zaliczka_CO:.2f} [GJ]')
                                p.drawString(480, 415, f'{zaliczka_CO * stawka_CO_miernik:.2f} zł')
                        else:
                            p.drawString(390, 415, f'------')
                            p.drawString(480, 415, f'------')
                        if stawka_cw != 0:
                            p.drawString(285, 397, f'{stawka_cw:.2f} zł')
                        else:
                            p.drawString(290, 397, f'------')
                        if stawka_cw != 0 or zaliczka_cw != 0:
                            p.drawString(480, 397, f'{zaliczka_cw * stawka_cw:.2f} zł')
                        else:
                            p.drawString(480, 397, f'------')
                        if stawka_zw != 0 or stawka_scieki != 0:
                            p.drawString(288, 307, f'{stawka_zw + stawka_scieki:.2f} zł')
                        else:
                            p.drawString(288, 307, f'------')
                        if stawka_zw != 0 or stawka_scieki != 0 or zaliczka_uchyl_wody != 0:
                            p.drawString(480, 307, f'{(stawka_zw + stawka_scieki) * zaliczka_uchyl_wody:.2f} zł')
                        else:
                            p.drawString(480, 307, f'------')
                        if stawka_miejsce_postojowe_komorka != 0:
                            p.drawString(288, 289, f'{stawka_miejsce_postojowe_komorka:.2f} zł')
                        else:
                            p.drawString(290, 289, f'------')
                        if stawka_miejsce_postojowe_komorka != 0 or zaliczka_miejsce_postojowe_komorka != 0:
                            p.drawString(480, 289, f'{zaliczka_miejsce_postojowe_komorka * stawka_miejsce_postojowe_komorka:.2f} zł')
                        else:
                            p.drawString(480, 289, f'------')
                        if stawka_zw != 0:
                            p.drawString(288, 379, f'{stawka_zw:.2f} zł')
                        else:
                            p.drawString(290, 379, f'------')
                        if stawka_zw != 0 or zaliczka_zw != 0:
                            p.drawString(480, 379, f'{zaliczka_zw * stawka_zw:.2f} zł')
                        else:
                            p.drawString(480, 370, f'------')
                        if stawka_scieki != 0:
                            p.drawString(288, 361, f'{stawka_scieki:.2f} zł')
                        else:
                            p.drawString(290, 361, f'------')
                        if stawka_scieki != 0 or zaliczka_scieki != 0:
                            p.drawString(480, 361, f'{zaliczka_scieki * stawka_scieki:.2f} zł')
                        else:
                            p.drawString(480, 361, f'------')
                        if stawka_nieczystosci == 11:
                            if osoby == 1:
                                odpady = stawka_nieczystosci * osoby
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 2:
                                odpady = stawka_nieczystosci * osoby - 1
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 3:
                                odpady = stawka_nieczystosci * osoby - 3
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby >= 4:
                                odpady = stawka_nieczystosci * 4 - 6
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 0:
                                odpady = 0
                                p.drawString(480, 343, f'0.00 zł')
                                p.drawString(285, 343, f'11.00 zł')
                        if stawka_nieczystosci == 14:
                            if osoby == 1:
                                odpady = stawka_nieczystosci * osoby
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 2:
                                odpady = stawka_nieczystosci * osoby - 1
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 3:
                                odpady = stawka_nieczystosci * osoby - 4
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby >= 4:
                                odpady = stawka_nieczystosci * 4 - 8
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 0:
                                odpady = 0
                                p.drawString(480, 343, f'0.00 zł')
                                p.drawString(285, 343, f'14.00 zł')
                        if stawka_winda != 0:
                            p.drawString(288, 325, f'{stawka_winda:.2f} zł')
                        else:
                            p.drawString(290, 325, f'------')
                        if stawka_winda != 0 or winda != 0:
                            p.drawString(480, 325, f'{stawka_winda * winda:.2f} zł')
                        else:
                            p.drawString(480, 325, f'------')
                        if stawka_fundusz_remontowy != 0:
                            p.drawString(288, 222, f'{stawka_fundusz_remontowy:.2f} zł')
                        else:
                            p.drawString(290, 222, f'------')
                        if stawka_fundusz_remontowy != 0 or powierzchnia != 0:
                            p.drawString(480, 222, f'{stawka_fundusz_remontowy * powierzchnia:.2f} zł')
                        else:
                            p.drawString(480, 222, f'------')
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        if stawka_CO_miernik == 0:
                            s1 = float(str(f'{stawka_eksploatacja * powierzchnia:.2f}'))
                            s2 = float(str(f'{zaliczka_CO:.2f}'))
                            s3 = float(str(f'{stawka_cw * zaliczka_cw:.2f}'))
                            s4 = float(str(f'{stawka_zw * zaliczka_zw:.2f}'))
                            s5 = float(str(f'{stawka_scieki * zaliczka_scieki:.2f}'))
                            s6 = float(str(f'{odpady:.2f}'))
                            s7 = float(str(f'{stawka_winda * winda:.2f}'))
                            s8 = float(str(f'{(stawka_scieki + stawka_zw) * zaliczka_uchyl_wody:.2f}'))
                            s9 = float(
                                str(f'{stawka_miejsce_postojowe_komorka * zaliczka_miejsce_postojowe_komorka:.2f}'))
                            p.drawString(480, 270,
                                         f'{s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9:.2f} zł')
                        else:
                            s1 = float(str(f'{stawka_eksploatacja * powierzchnia:.2f}'))
                            s2 = float(str(f'{zaliczka_CO * stawka_CO_miernik:.2f}'))
                            s3 = float(str(f'{stawka_cw * zaliczka_cw:.2f}'))
                            s4 = float(str(f'{stawka_zw * zaliczka_zw:.2f}'))
                            s5 = float(str(f'{stawka_scieki * zaliczka_scieki:.2f}'))
                            s6 = float(str(f'{odpady:.2f}'))
                            s7 = float(str(f'{stawka_winda * winda:.2f}'))
                            s8 = float(str(f'{(stawka_scieki + stawka_zw) * zaliczka_uchyl_wody:.2f}'))
                            s9 = float(
                                str(f'{stawka_miejsce_postojowe_komorka * zaliczka_miejsce_postojowe_komorka:.2f}'))
                            p.drawString(480, 270,
                                         f'{s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9:.2f} zł')
                    else:
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        p.drawString(122, 510, f'{data_poczatek_oplat} r.')
                        p.drawString(243, 510, f'{data_koniec_oplat} r.')
                        p.setFont("DejaVuSans", 10, leading=None)
                        p.drawString(80, 510,
                                     f'Od dnia                          do dnia                          miesięczne należności wynoszą:')
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        if stawka_fundusz_remontowy != 0 or powierzchnia != 0:
                            p.drawString(480, 204, f'{stawka_fundusz_remontowy * powierzchnia * procent:.2f} zł')
                        else:
                            p.drawString(480, 204, f'------')
                        p.setFont("DejaVuSans", 10, leading=None)
                        if stawka_eksploatacja != 0 or powierzchnia != 0:
                            p.drawString(268, 433,
                                         f'{stawka_eksploatacja:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                            p.drawString(480, 433, f'{powierzchnia * stawka_eksploatacja * procent:.2f} zł')
                        else:
                            p.drawString(290, 433, f'------')
                            p.drawString(480, 433, f'------')
                        if zaliczka_CO != 0:
                            if stawka_CO_miernik == 0:
                                p.drawString(362, 415,
                                             f'{zaliczka_CO:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                                p.drawString(480, 415, f'{zaliczka_CO * procent:.2f} zł')
                            else:
                                p.drawString(378, 415,
                                             f'{zaliczka_CO:.2f} [GJ]')
                                p.drawString(265, 415,
                                             f'{stawka_CO_miernik:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                                p.drawString(480, 415, f'{zaliczka_CO * stawka_CO_miernik * procent:.2f} zł')
                        else:
                            p.drawString(390, 415, f'------')
                            p.drawString(480, 415, f'------')
                        if stawka_cw != 0:
                            p.drawString(265, 397, f'{stawka_cw:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                            p.drawString(480, 397, f'{zaliczka_cw * stawka_cw * procent:.2f} zł')
                        else:
                            p.drawString(290, 397, f'------')
                            p.drawString(480, 397, f'------')
                        if stawka_zw != 0:
                            p.drawString(268, 379, f'{stawka_zw:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                            p.drawString(480, 379, f'{zaliczka_zw * stawka_zw * procent:.2f} zł')
                        else:
                            p.drawString(290, 379, f'------')
                            p.drawString(480, 379, f'------')
                        if stawka_scieki != 0:
                            p.drawString(268, 361, f'{stawka_scieki:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                            p.drawString(480, 361, f'{zaliczka_scieki * stawka_scieki * procent:.2f} zł')
                        else:
                            p.drawString(290, 361, f'------')
                            p.drawString(480, 361, f'------')
                        if stawka_zw != 0 or stawka_scieki != 0:
                            p.drawString(268, 307, f'{stawka_zw + stawka_scieki:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                        else:
                            p.drawString(290, 307, f'------')
                        if stawka_zw != 0 or stawka_scieki != 0 or zaliczka_uchyl_wody != 0:
                            p.drawString(480, 307, f'{(stawka_zw + stawka_scieki) * zaliczka_uchyl_wody * procent:.2f} zł')
                        else:
                            p.drawString(480, 307, f'------')
                        if stawka_miejsce_postojowe_komorka != 0:
                            p.drawString(268, 289, f'{stawka_miejsce_postojowe_komorka:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                        else:
                            p.drawString(290, 289, f'------')
                        if stawka_miejsce_postojowe_komorka != 0 or zaliczka_miejsce_postojowe_komorka != 0:
                            p.drawString(480, 289, f'{zaliczka_miejsce_postojowe_komorka * stawka_miejsce_postojowe_komorka * procent:.2f} zł')
                        else:
                            p.drawString(480, 289, f'------')
                        if stawka_nieczystosci == 11:
                            if osoby == 1:
                                odpady = stawka_nieczystosci * osoby
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 2:
                                odpady = stawka_nieczystosci * osoby - 1
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 3:
                                odpady = stawka_nieczystosci * osoby - 3
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby >= 4:
                                odpady = stawka_nieczystosci * 4 - 6
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 0:
                                odpady = 0
                                p.drawString(480, 343, f'0.00 zł')
                                p.drawString(285, 343, f'11.00 zł')
                        if stawka_nieczystosci == 14:
                            if osoby == 1:
                                odpady = stawka_nieczystosci * osoby
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 2:
                                odpady = stawka_nieczystosci * osoby - 1
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 3:
                                odpady = stawka_nieczystosci * osoby - 4
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby >= 4:
                                odpady = stawka_nieczystosci * 4 - 8
                                p.drawString(480, 343, f'{odpady:.2f} zł')
                                p.drawString(285, 343, f'{odpady:.2f} zł')
                            elif osoby == 0:
                                odpady = 0
                                p.drawString(480, 343, f'0.00 zł')
                                p.drawString(285, 343, f'14.00 zł')
                        if stawka_winda != 0:
                            p.drawString(268, 325, f'{stawka_winda:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                            p.drawString(480, 325, f'{stawka_winda * winda * procent:.2f} zł')
                        else:
                            p.drawString(290, 325, f'------')
                            p.drawString(480, 325, f'------')
                        if stawka_fundusz_remontowy != 0 or powierzchnia != 0:
                            p.drawString(268, 222,
                                         f'{stawka_fundusz_remontowy:.2f} zł x {ilosc_dni_oplat}/{ilosc_dni_w_miesiacu}')
                            p.drawString(480, 222, f'{stawka_fundusz_remontowy * powierzchnia * procent:.2f} zł')
                        else:
                            p.drawString(290, 222, f'------')
                            p.drawString(480, 222, f'------')
                        p.setFont("DejaVuSans-Bold", 10, leading=None)
                        if stawka_CO_miernik == 0:
                            s1 = float(str(f'{stawka_eksploatacja * powierzchnia * procent:.2f}'))
                            s2 = float(str(f'{zaliczka_CO * procent:.2f}'))
                            s3 = float(str(f'{stawka_cw * zaliczka_cw * procent:.2f}'))
                            s4 = float(str(f'{stawka_zw * zaliczka_zw * procent:.2f}'))
                            s5 = float(str(f'{stawka_scieki * zaliczka_scieki * procent:.2f}'))
                            s6 = float(str(f'{odpady:.2f}'))
                            s7 = float(str(f'{stawka_winda * winda * procent:.2f}'))
                            s8 = float(str(f'{(stawka_scieki + stawka_zw) * zaliczka_uchyl_wody * procent:.2f}'))
                            s9 = float(
                                str(
                                    f'{stawka_miejsce_postojowe_komorka * zaliczka_miejsce_postojowe_komorka * procent:.2f}'))
                            p.drawString(480, 270,
                                         f'{s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9:.2f} zł')
                        else:
                            s1 = float(str(f'{stawka_eksploatacja * powierzchnia * procent:.2f}'))
                            s2 = float(str(f'{zaliczka_CO * stawka_CO_miernik * procent:.2f}'))
                            s3 = float(str(f'{stawka_cw * zaliczka_cw * procent:.2f}'))
                            s4 = float(str(f'{stawka_zw * zaliczka_zw * procent:.2f}'))
                            s5 = float(str(f'{stawka_scieki * zaliczka_scieki * procent:.2f}'))
                            s6 = float(str(f'{odpady:.2f}'))
                            s7 = float(str(f'{stawka_winda * winda * procent:.2f}'))
                            s8 = float(str(f'{(stawka_scieki + stawka_zw) * zaliczka_uchyl_wody * procent:.2f}'))
                            s9 = float(
                                str(
                                    f'{stawka_miejsce_postojowe_komorka * zaliczka_miejsce_postojowe_komorka * procent:.2f}'))
                            p.drawString(480, 270,
                                         f'{s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9:.2f} zł')
                        p.setFont("DejaVuSans", 10, leading=None)
                    p.showPage()
    else:
        p.setFont("DejaVuSans-Bold", 14, leading=None)
        p.drawString(40, 720, f'BŁĄD:')
        p.drawString(40, 700, f'Data końca naliczenia jest wcześniejsza niż data rozpoczęcia')
        p.drawString(40, 680, f'naliczenia.')
        p.setFont("DejaVuSans", 10, leading=None)
        p.drawString(40, 640, f'ZASADY USTAWIANIA DAT PRZY TWORZENIU NALICZEŃ:')
        p.drawString(50, 625, f'1.  Gdy okres obowiązywania naliczenia ma być dłuższy niż 1 miesiąc, to data')
        p.drawString(55, 610, f'rozpoczęcia opłat musi być ustawiona na pierwszy dzień miesiąca, a data końca')
        p.drawString(55, 595, f'opłat musi być ustawiona na ostatni dzień miesiąca - najlepiej dla jakiejś')
        p.drawString(55, 580, f'bardzo odległej daty.')
        p.drawString(50, 565, f'2.  Gdy wiadomo kiedy kończy się czas trwania naliczenia obejmującego okres')
        p.drawString(55, 550, f'większy niż jeden miesiąc, należy edytować formularz naliczenia i ustawić datę')
        p.drawString(55, 535, f'końca trwania naliczenia na właściwą')
        p.drawString(50, 520, f'3.  Gdy naliczenie obejmuje okres krótszy niż 1 miesiąc, to miesiąć początka i końca')
        p.drawString(55, 505, f'opłat powinny być takie same.')
    if data_poczatek_oplat < data_koniec_oplat and ilosc_dodanych_do_naliczenia_wlascicieli == 0 and licznik_braku_dodanych_wlascicieli == 0:
        p.setFont("DejaVuSans-Bold", 14, leading=None)
        p.drawString(40, 720, f'BŁĄD:')
        p.drawString(40, 700, f'Dla podanego okresu naliczenia właściciel')
        p.drawString(40, 680, f'nie posiada obowiązujących danych.')
        p.drawString(40, 660, f'Ustaw poprawnie daty początku i końca naliczeń')
        p.drawString(40, 640, f'i/lub sprawdź dla właściciela')
        p.drawString(40, 620, f'dla którego tworzone jest naliczenie,')
        p.drawString(40, 600, f'ustawienia dat: "dane od" i "dane do".')
    p.save()
    return response