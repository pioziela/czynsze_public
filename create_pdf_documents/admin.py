from django.contrib import admin
from .models import Naliczenie_cala_wspolnota, Mieszkaniec, Wspolnota, Naliczenie_jeden_mieszkaniec
import django.contrib.admin.options as admin_opt


def dup_event(modeladmin:admin_opt.ModelAdmin, request, queryset):
    for object in queryset:
        from_id = object.id
        object.id = None
        object.save()
        message="dup from {} to {}".format(from_id, object.id)
        modeladmin.log_addition(request=request,object=object,message=message)


dup_event.short_description = "Duplicate Records"


class MieszkaniecAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id', 'imie', 'nazwisko', 'wspolnota',)
    list_filter = ('imie','wspolnota',)
    search_fields = ('imie','wspolnota')
    ordering = ['id']
    actions = [dup_event]


class Naliczenie_cala_wspolnotaAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id','data_dokumentu', 'wspolnota', 'data_utworzenia')
    ordering = ['id']
    actions = [dup_event]


class Naliczenie_jeden_mieszkaniecAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id','data_dokumentu', 'wlasciciel',)
    ordering = ['id']
    actions = [dup_event]


class WspolnotaAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id','wspolnota',)
    ordering = ['wspolnota']
    actions = [dup_event]


admin.site.register(Mieszkaniec, MieszkaniecAdmin)
admin.site.register(Naliczenie_cala_wspolnota, Naliczenie_cala_wspolnotaAdmin)
admin.site.register(Wspolnota, WspolnotaAdmin)
admin.site.register(Naliczenie_jeden_mieszkaniec, Naliczenie_jeden_mieszkaniecAdmin)
