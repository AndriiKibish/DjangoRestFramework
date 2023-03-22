from django.http import HttpResponse

from carsapi.models import Car
from rest_framework import viewsets
from carsapi.serializers import CarModelSerializer
import csv


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-year')
    serializer_class = CarModelSerializer


def run_str_to_int(a: str) -> int:
    x = (f'{a}'.split())
    y = int(x[0].replace(',', ''))
    return y


def lakh_usd(a: str) -> int:
    x = (f'{a}'.split())
    y = int(float(x[0]) * 1207)
    return y


def upload_data(request):
    with open('carsapi/car_price.csv') as f:
        for row in csv.reader(f):
            # print(row)
            try:
                _, created = Car.objects.get_or_create(
                    name=row[1],
                    price=lakh_usd(row[2]),
                    kms_driven=run_str_to_int(row[3]),
                    fuel_type=row[4],
                    transmission=row[5],
                    year=int(row[7]),
                    engine_vol=int(row[8].split()[0]),
                    seats=int(row[9].split()[0]),
                )
            except:
                pass
        return HttpResponse("Done!")
