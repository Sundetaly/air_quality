from typing import List

from pandas import DataFrame

from main.models import Pesticide
from main.serializers import PesticideSerializer


def import_district(df: DataFrame) -> List[Pesticide]:
    df = df.drop(columns=['ID'])
    district_arr = []
    for _, raw in df.iterrows():
        district_data = dict()
        district_data['name'] = raw['Место расположение']
        district_data['count_pesticide'] = raw['Количество пестицидов, кг']
        district_data['name_pesticide'] = raw['Наименование пестицидов']
        district_data['name_banned_pesticide'] = raw['Наименование запрещенных пестицидов']
        district_arr.append(district_data)
    serializer = PesticideSerializer(data=district_arr, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
