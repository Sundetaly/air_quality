from typing import List

from pandas import DataFrame

from main.models import CommonPesticide
from main.serializers import DistrictSerializer

#
# def import_city(df: DataFrame) -> List[City]:
#     df = df.drop(columns=['ID'])
#     city_arr = []
#     for _, raw in df.iterrows():
#         city_data = dict()
#         city_data['name'] = raw['Город']
#         city_data['pollution_level_00'] = raw['Уровень загрязнения атмосферного воздуха в 2000 г']
#         city_data['pollution_level_01'] = raw['Уровень загрязнения атмосферного воздуха в 2001 г']
#         city_data['pollution_level_02'] = raw['Уровень загрязнения атмосферного воздуха в 2002 г']
#         city_data['industries'] = raw['Отрасли промышленности, оказывающие влияние на загрязнение воздуха']
#         city_arr.append(city_data)
#     serializer = CitySerializer(data=city_arr, many=True)
#     serializer.is_valid(raise_exception=True)
#     return serializer.save()


def import_district(df: DataFrame) -> List[CommonPesticide]:
    df = df.drop(columns=['ID'])
    district_arr = []
    for _, raw in df.iterrows():
        district_data = dict()
        district_data['name'] = raw['Место расположение']
        district_data['count_pesticide'] = raw['Количество пестицидов, кг']
        district_data['name_pesticide'] = raw['Наименование пестицидов']
        district_data['name_banned_pesticide'] = raw['Наименование запрещенных пестицидов']
        district_arr.append(district_data)
    serializer = DistrictSerializer(data=district_arr, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
