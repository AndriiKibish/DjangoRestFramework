from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    kms_driven = models.IntegerField()
    fuel_type = models.CharField(max_length=20)
    transmission = models.CharField(max_length=20)
    year = models.IntegerField()
    engine_vol = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.id}_{self.name}"
