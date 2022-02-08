from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import *

admin.site.register(Region)

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Pesticide)
class PesticideAdmin(admin.ModelAdmin):
    list_display = ("region", "location", "count_pesticide", "name_pesticide", "name_banned_pesticide")
    list_filter = ("region", "location", "count_pesticide", "name_pesticide", "name_banned_pesticide")


admin.site.register(StorageStatus)
admin.site.register(Analysis)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "location", "status", "add_info", "obsolete_pesticides", "year")
    list_filter = ("name", "region", "location", "status", "add_info", "obsolete_pesticides", "year")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("region", "number_rooms", "number_un_rooms", "number_limit_pdk", "number_above_pdk")
    list_filter = ("region", "number_rooms", "number_un_rooms", "number_limit_pdk", "number_above_pdk")


admin.site.register(FormPreparation)
admin.site.register(TypeContainer)


@admin.register(Preparation)
class PreparationAdmin(admin.ModelAdmin):
    list_display = ("region", "location", "name_location", "trade_name", "number", "form", "type_container",
                    "status_container", "import_year", "birth", "add_info", "note")
    list_filter = ("region", "location", "name_location", "trade_name", "number", "form", "type_container",
                   "status_container", "import_year", "birth", "add_info", "note")








