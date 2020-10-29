from django import forms
from django.contrib.auth.forms import UsernameField, ReadOnlyPasswordHashField
from django.contrib.auth import (authenticate, get_user_model)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from .models import Mieszkaniec, Wspolnota, Naliczenie_cala_wspolnota, \
    Naliczenie_jeden_mieszkaniec

UserModel = get_user_model()


class DateInput(forms.DateInput):
    input_type = "date"


class MieszkaniecForm(ModelForm):
    date = str(datetime.today().strftime("%Y-%m-%d"))
    aktywny_od = forms.DateField(widget=DateInput, initial=f'{date}', label='Aktywny od:')
    aktywny_do = forms.DateField(widget=DateInput, initial="2050-01-31", label='Aktywny do:')
    dane_od = forms.DateField(widget=DateInput, initial=f"{date}", label='Dane ważne od:')
    dane_do = forms.DateField(widget=DateInput, initial="2050-01-31", label='Dane ważne do:')
    class Meta:
        model = Mieszkaniec
        fields = ['imie', 'nazwisko', 'wspolnota', 'adres_ulica', 'adres_numer_domu',
                  'adres_numer_mieszkania', 'kod_pocztowy', 'miasto', 'powierzchnia_mieszkania',
                  'zaliczka_CO', 'zaliczka_CO_miernik', 'podgrzanie_wody_objetosc', 'zimna_woda_objetosc',
                  'odprowadzenie_sciekow_objetosc', 'uchyl_wody', 'miejsce_postojowe_komorka', 'ilosc_osob', 'winda','aktywny_od', 'aktywny_do',
                  'dane_od', 'dane_do']


class WspolnotaForm(ModelForm):
    date = str(datetime.today().strftime("%Y-%m-%d"))
    aktywny_od = forms.DateField(widget=DateInput, initial=f"{date}", label='Aktywna od:')
    aktywny_do = forms.DateField(widget=DateInput, initial="2050-01-31", label='Aktywna do:')
    class Meta:
        model = Wspolnota
        fields = ['wspolnota','konto_eksploatacyjne','konto_remontowe', 'adres_ulica', 'adres_numer_domu',
                  'kod_pocztowy', 'miasto', 'aktywny_od', 'aktywny_do']


class Naliczenie_cala_wspolnotaForm(forms.ModelForm):
    date = str(datetime.today().strftime("%Y-%m-%d"))
    date2 = datetime.today()
    month, year = date2.month, date2.year
    if month < 12:
        data_obowiazywania_oplat = forms.DateField(widget=DateInput, initial=f"{year}-{month+1}-01",label='Początkowa data obowiązywania opłat:')
    if month == 12:
        data_obowiazywania_oplat = forms.DateField(widget=DateInput, initial=f"{year+1}-01-01",label='Początkowa data obowiązywania opłat:')
    data_dokumentu = forms.DateField(widget=DateInput, initial=f"{date}", label='Data wystawienia dokumentu:')
    oplaty_do = forms.DateField(widget=DateInput, initial="2050-01-31", label='Końcowa data obowiązywania opłat (gdy nieznana: 31.01.2050, pamiętać by ustawić poprawnie gdy jest już znana):')

    class Meta:
        model = Naliczenie_cala_wspolnota
        fields = ['data_dokumentu','wspolnota','data_obowiazywania_oplat', 'oplaty_do', 'zmianie_ulegaja_oplaty_za',
                  'stawka_zaliczka_eksploatacyjna','stawka_CO_miernik', 'stawka_podgrzanie_wody', 'stawka_zimna_woda',
                  'stawka_odprowadzenie_sciekow', 'stawka_wywoz_nieczystosci', 'stawka_winda', 'stawka_miejsce_postojowe_komorka',
                  'stawka_fundusz_remontowy', 'dodatkowa_informacja_gora', 'dodatkowa_informacja_dol', 'dodatkowa_informacja_dol_2']


class Naliczenie_jeden_mieszkaniecForm(ModelForm):
    date = str(datetime.today().strftime("%Y-%m-%d"))
    date2 = datetime.today()
    month, year = date2.month, date2.year
    if month < 12:
        data_obowiazywania_oplat = forms.DateField(widget=DateInput, initial=f"{year}-{month+1}-01",label='Początkowa data obowiązywania opłat:')
    if month == 12:
        data_obowiazywania_oplat = forms.DateField(widget=DateInput, initial=f"{year+1}-01-01",label='Początkowa data obowiązywania opłat:')
    data_dokumentu = forms.DateField(widget=DateInput, initial=f"{date}", label='Data wystawienia dokumentu:')
    oplaty_do = forms.DateField(widget=DateInput, initial="2050-01-31", label='Końcowa data obowiązywania opłat (gdy nieznana: 31.01.2050, pamiętać by ustawić poprawnie gdy jest już znana):')

    class Meta:
        model = Naliczenie_jeden_mieszkaniec
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wlasciciel'].queryset = Mieszkaniec.objects.none()
        if 'wspolnota' in self.data:
            try:
                wspolnota_id = int(self.data.get('wspolnota'))
                self.fields['wlasciciel'].queryset = Mieszkaniec.objects.filter(wspolnota_id=wspolnota_id).order_by('wspolnota')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['wlasciciel'].queryset = self.instance.wspolnota.mieszkaniec_set.order_by('wspolnota')


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _(
            "Podaj prawidłową nazwę użytkownika i hasło."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields['username'].max_length = username_max_length
        self.fields['username'].widget.attrs['maxlength'] = username_max_length
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.
        If the given user cannot log in, this method should raise a
        ``ValidationError``.
        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial.get('password')


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Użytkownik:',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = UsernameField(
        label='Hasło:',
        widget=forms.PasswordInput(attrs={'autofocus': True})
    )