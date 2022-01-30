from typing import List

from pandas import DataFrame

from main.models import Pesticide, Region, Storage, Analysis, \
    StorageStatus, Room, FormPreparation, TypeContainer
from main.serializers import PesticideImportSerializer, StorageImportSerializer, \
    RoomImportSerializer, PreparationImportSerializer


def get_or_create_region(region: str):
    region, _ = Region.objects.get_or_create(name=region)
    return region


def get_or_create_analysis(year: str):
    analysis, _ = Analysis.objects.get_or_create(year=year)
    return analysis


def get_or_create_status(name: str):
    status, _ = StorageStatus.objects.get_or_create(name=name)
    return status


def get_or_create_form(name: str):
    form, _ = FormPreparation.objects.get_or_create(name=name)
    return form


def get_or_create_type(name: str):
    type_container, _ = TypeContainer.objects.get_or_create(name=name)
    return type_container


def import_pesticide(df: DataFrame) -> List[Pesticide]:
    df = df.drop(columns=['ID'])
    pesticide_arr = []
    for _, raw in df.iterrows():
        pesticide_data = dict()
        pesticide_data['location'] = raw['Место расположение']
        pesticide_data['count_pesticide'] = raw['Кол-во пестицидов, кг']
        pesticide_data['name_pesticide'] = raw['Наименование пестицидов']
        pesticide_data['name_banned_pesticide'] = raw['Наименование запрещенных пестицидов']
        pesticide_data["region"] = get_or_create_region(raw['Район']).id
        pesticide_arr.append(pesticide_data)

    serializer = PesticideImportSerializer(data=pesticide_arr, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def import_storage(df: DataFrame) -> List[Storage]:
    df = df.drop(columns=['ID'])
    storage_arr = []
    for _, raw in df.iterrows():
        storage_data = dict()
        storage_data['region'] = get_or_create_region(raw['Район']).id
        storage_data['location'] = raw['Месторасположение хранилище']
        storage_data['name'] = raw['Название хранилища']
        storage_data['status'] = get_or_create_status(raw['Состояние хранилища']).id
        storage_data['add_info'] = raw['Дополнительная информация']
        storage_data['obsolete_pesticides'] = raw['Устаревшие пестициды, кг']
        storage_data['year'] = get_or_create_analysis(raw['Год исследование']).id
        storage_arr.append(storage_data)

    serializer = StorageImportSerializer(data=storage_arr, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def import_room(df: DataFrame) -> List[Room]:
    room_arr = []
    for _, raw in df.iterrows():
        room_data = dict()
        print(raw)
        room_data['region'] = get_or_create_region('Карасайский').id
        room_data['number_rooms'] = raw['Количество складских помещений']
        room_data['number_un_rooms'] = raw['Количество складских помещений без загрязнения']
        room_data['number_limit_pdk'] = raw['Количество территории, где количество пестицидов в пределах ПДК']
        room_data['number_above_pdk'] = raw['Количество территории, где количество пестицидов выше ПДК']
        room_arr.append(room_data)

    serializer = RoomImportSerializer(data=room_arr, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def import_preparation(df: DataFrame) -> List[Room]:
    preparation_arr = []
    for _, raw in df.iterrows():
        preparation_data = dict()
        preparation_data['region'] = get_or_create_region('Карасайский').id
        preparation_data['location'] = raw['Месторасположение хранилища']
        preparation_data['name_location'] = raw['Название хранилища']
        preparation_data['trade_name'] = raw['Торговое название']
        preparation_data['number'] = raw['Количество']
        preparation_data['form'] = get_or_create_form(raw['Препаративная форма']).id
        preparation_data['type_container'] = get_or_create_type(raw['Тип контейнера']).id
        preparation_data['status_container'] = get_or_create_type(raw['Состояние контейнера']).id
        preparation_data['import_year'] = raw['Год ввоза']
        preparation_data['birth'] = raw['Происхождение']
        preparation_data['add_info'] = raw['Дополнительная информация']
        preparation_data['note'] = raw['Замечания']

        preparation_arr.append(preparation_data)

    serializer = PreparationImportSerializer(data=preparation_arr, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

