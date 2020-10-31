from django.db import models


class Wspolnota(models.Model):
    wspolnota = models.CharField(max_length=300, null=True, unique=True, verbose_name='Wspólnota:')
    konto_eksploatacyjne = models.CharField(max_length=100, verbose_name='Konto eksploatacyjne:')
    konto_remontowe = models.CharField(max_length=100, verbose_name='Konto remontowe (jeśli nie ma, wpisz: "brak"):')
    adres_ulica = models.CharField(max_length=50, verbose_name="Ulica:")
    adres_numer_domu = models.CharField(max_length=50, verbose_name="Numer domu:")
    kod_pocztowy = models.CharField(max_length=20, verbose_name="Kod pocztowy:")
    miasto = models.CharField(max_length=30, verbose_name="Miasto:")
    aktywny_od = models.DateField(verbose_name="Aktywna od:")
    aktywny_do = models.DateField(verbose_name="Aktywna do:")

    class Meta:
        ordering = ['wspolnota']

    def __str__(self):
        return self.wspolnota


class Mieszkaniec(models.Model):
    imie = models.CharField(max_length=30, verbose_name="Imię:")
    nazwisko = models.CharField(max_length=50, verbose_name="Nazwisko:")
    wspolnota = models.ForeignKey(Wspolnota, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Wspólnota:")
    adres_ulica = models.CharField(max_length=50, verbose_name="Ulica:")
    adres_numer_domu = models.CharField(max_length=50, verbose_name="Numer domu:")
    adres_numer_mieszkania = models.PositiveSmallIntegerField(verbose_name="Numer mieszkania:")
    kod_pocztowy = models.CharField(max_length=20, verbose_name="Kod pocztowy:")
    miasto = models.CharField(max_length=30, verbose_name="Miasto:")
    powierzchnia_mieszkania = models.FloatField(verbose_name="Powierzchnia mieszkania [m2]:")
    zaliczka_CO = models.FloatField(default=0, verbose_name="Zaliczka C.O. [zł] PODZIELNIK (gdy nie dotyczy zostaw 0):")
    zaliczka_CO_miernik = models.FloatField(default=0, verbose_name="Zaliczka C.O. [GJ] LICZNIK (gdy nie dotyczy zostaw 0):")
    podgrzanie_wody_objetosc = models.FloatField(verbose_name="Ciepła woda [m3]:")
    zimna_woda_objetosc = models.FloatField(verbose_name="Zimna woda [m3]:")
    odprowadzenie_sciekow_objetosc = models.FloatField(verbose_name="Ścieki [m3]:")
    uchyl_wody = models.FloatField(default=0, verbose_name="Uchył wody [m3]:")
    miejsce_postojowe_komorka = models.FloatField(default=0, verbose_name="Powierzchnia miejsce postojowe/komórka [m2]:")
    ilosc_osob = models.PositiveSmallIntegerField(verbose_name="Osoby:")
    winda = models.PositiveSmallIntegerField(verbose_name="Winda (osoby):")
    aktywny_od = models.DateField(verbose_name="Aktywny od:")
    aktywny_do = models.DateField(verbose_name="Aktywny do:")
    dane_od = models.DateField(verbose_name="Dane ważne od:")
    dane_do = models.DateField(verbose_name="Dane ważne do:")

    def __str__(self):
        return self.nazwisko+" "+self.imie


class Naliczenie_cala_wspolnota(models.Model):
    smieci = [
        (11, 11),
        (14, 14),
    ]
    data_dokumentu = models.DateField(verbose_name='Data wystawienia dokumentu:')
    wspolnota = models.ForeignKey(Wspolnota, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Wspólnota:')
    data_utworzenia = models.DateField(auto_now_add=True)
    data_obowiazywania_oplat = models.DateField(verbose_name='Początkowa data obowiązywania opłat:')
    oplaty_do = models.DateField(verbose_name='Końcowa data obowiązywania opłat (gdy nieznana: 2050-01-01, pamiętać by ustawić poprawnie gdy jest już znana):')
    zmianie_ulegaja_oplaty_za = models.CharField(max_length=300, verbose_name='Zmianie ulegają opłaty za (gdy jest to naliczenie dla nowej wspólnoty wpisz: "nic"):')
    stawka_zaliczka_eksploatacyjna = models.FloatField(verbose_name='Stawka eksploatacja [zł]:')
    stawka_CO_miernik = models.FloatField(default=0, verbose_name='Stawka C.O. [zł] LICZNIK (gdy nie dotyczy zostaw 0):')
    stawka_podgrzanie_wody = models.FloatField(verbose_name='Stawka ciepła woda [zł]:')
    stawka_zimna_woda = models.FloatField(verbose_name='Stawka zimna woda [zł]:')
    stawka_odprowadzenie_sciekow = models.FloatField(verbose_name='Stawka ścieki [zł]:')
    stawka_wywoz_nieczystosci = models.FloatField(choices=smieci, default=smieci[0][1], verbose_name='Stawka wywóz nieczystości [zł] (wybierz kwotę dla gospodarstwa 1-osobowego):')
    stawka_winda = models.FloatField(verbose_name='Stawka winda [zł]:')
    stawka_miejsce_postojowe_komorka = models.FloatField(default=0, verbose_name="Stawka miejsce postojowe/komórka [zł]:")
    stawka_fundusz_remontowy = models.FloatField(verbose_name='Stawka fundusz remontowy [zł]:')
    dodatkowa_informacja_gora = models.CharField(max_length=300, default='brak', verbose_name='Treść dodatkowej informacji do umieszczenia w dokumencie na górze (w przypadku jej braku pozostawić "brak"):')
    dodatkowa_informacja_dol = models.CharField(max_length=300, default='brak', verbose_name='Treść dodatkowej informacji do umieszczenia w dokumencie na dole (w przypadku jej braku pozostawić "brak"):')
    dodatkowa_informacja_dol_2 = models.CharField(max_length=300, default='brak', verbose_name='Treść dodatkowej informacji do umieszczenia w dokumencie na dole w drugiej linii (w przypadku jej braku pozostawić "brak"):')


class Naliczenie_jeden_mieszkaniec(models.Model):
    smieci = [
        (11, 11),
        (14, 14),
    ]
    data_dokumentu = models.DateField()
    wspolnota = models.ForeignKey(Wspolnota, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Wspólnota')
    wlasciciel = models.ForeignKey(Mieszkaniec, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Właściciel')
    data_utworzenia = models.DateField(auto_now_add=True)
    data_obowiazywania_oplat = models.DateField()
    oplaty_do = models.DateField()
    zmianie_ulegaja_oplaty_za = models.CharField(max_length=300, verbose_name='Zmianie ulegają opłaty za (gdy jest to naliczenie dla nowego właściciela wpisz: "nic"):')
    stawka_zaliczka_eksploatacyjna = models.FloatField(verbose_name='Stawka eksploatacja [zł]:')
    stawka_CO_miernik = models.FloatField(default=0, verbose_name='Stawka C.O. [zł] LICZNIK (gdy nie dotyczy zostaw 0):')
    stawka_podgrzanie_wody = models.FloatField(verbose_name='Stawka ciepła woda [zł]:')
    stawka_zimna_woda = models.FloatField(verbose_name='Stawka zimna woda [zł]:')
    stawka_odprowadzenie_sciekow = models.FloatField(verbose_name='Stawka ścieki [zł]:')
    stawka_wywoz_nieczystosci = models.FloatField(choices=smieci, default=smieci[0][1], verbose_name='Stawka wywóz nieczystości [zł] (wybierz kwotę dla gospodarstwa 1-osobowego):')
    stawka_winda = models.FloatField(verbose_name='Stawka winda [zł]:')
    stawka_miejsce_postojowe_komorka = models.FloatField(default=0, verbose_name="Stawka miejsce postojowe/komórka [zł]:")
    stawka_fundusz_remontowy = models.FloatField(verbose_name='Stawka fundusz remontowy [zł]')
    dodatkowa_informacja_gora = models.CharField(max_length=300, default='brak', verbose_name='Treść dodatkowej informacji do umieszczenia w dokumencie na górze (w przypadku jej braku pozostawić "brak"):')
    dodatkowa_informacja_dol = models.CharField(max_length=300, default='brak', verbose_name='Treść dodatkowej informacji do umieszczenia w dokumencie na dole (w przypadku jej braku pozostawić "brak"):')
    dodatkowa_informacja_dol_2 = models.CharField(max_length=300, default='brak', verbose_name='Treść dodatkowej informacji do umieszczenia w dokumencie na dole w drugiej linii (w przypadku jej braku pozostawić "brak"):')


class Sortowanie(models.Model):
    parametry = [
        ('imie', 'imię'),
        ('nazwisko', 'nazwisko'),
        ('wspolnota', 'wspólnota'),
        ('numer_mieszkania', 'numer mieszkania'),
        ('miasto', 'miasto'),
        ('powierzchnia_mieszkania', 'powierzchnia mieszkania'),
        ('zaliczka_CO', 'zaliczka CO'),
        ('ciepla_woda', 'ciepła woda'),
        ('zimna_woda', 'zimna woda'),
        ('scieki', 'ścieki'),
        ('osoby', 'osoby'),
    ]
    parametry_sortowania = models.CharField(max_length=32,choices=parametry, default=parametry[2][0], verbose_name="")


class Sortowanie_naliczen_wspolnot(models.Model):
    parametry_wspolnot = [
        ('data_utworzenia', 'data utworzenia'),
        ('data_dokumentu', 'data dokumentu'),
        ('wspolnota', 'wspólnota'),
        ('data_obowiazywania_oplat','data obowiązywania opłat'),
        ('stawka_zaliczka_eksploatacyjna','stawka zaliczka eksploatacyjna'),
        ('stawka_podgrzanie_wody', 'stawka podgrzanie wody'),
        ('stawka_zimna_woda', 'stawka zimna woda'),
        ('stawka_odprowadzenie_sciekow', 'stawka odprowadzenie scieków'),
        ('stawka_wywoz_nieczystosci', 'stawka wywóz nieczystości'),
        ('stawka_winda', 'stawka winda'),
        ('stawka_fundusz_remontowy', 'stawka fundusz remontowy'),
    ]
    parametry_sortowania_wspolnot = models.CharField(max_length=300,choices=parametry_wspolnot, default=parametry_wspolnot[0][0], verbose_name="")


class Sortowanie_naliczen_wlascicieli(models.Model):
    parametry_wlascicieli = [
        ('data_utworzenia', 'data utworzenia'),
        ('data_dokumentu', 'data dokumentu'),
        ('wspolnota', 'wspólnota'),
        ('wlasciciel','właściciel'),
        ('data_obowiazywania_oplat','data obowiązywania opłat'),
        ('stawka_zaliczka_eksploatacyjna','stawka zaliczka eksploatacyjna'),
        ('stawka_podgrzanie_wody', 'stawka podgrzanie wody'),
        ('stawka_zimna_woda', 'stawka zimna woda'),
        ('stawka_odprowadzenie_sciekow', 'stawka odprowadzenie ściekow'),
        ('stawka_wywoz_nieczystosci', 'stawka wywóz nieczystości'),
        ('stawka_winda', 'stawka winda'),
        ('stawka_fundusz_remontowy', 'stawka fundusz remontowy'),
    ]
    parametry_sortowania_wlascicieli = models.CharField(max_length=300,choices=parametry_wlascicieli, default=parametry_wlascicieli[0][0], verbose_name="")


class Wyszukaj(models.Model):
    wyszukaj = models.CharField(max_length=32, default=None, verbose_name='')


class Wybor(models.Model):
    wybor_wspolnoty = models.ForeignKey(Wspolnota, on_delete=models.SET_NULL, null=True, verbose_name='')