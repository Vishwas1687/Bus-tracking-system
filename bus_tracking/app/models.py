from django.db import models


# Create your models here.
class Stops(models.Model):
    stop_id = models.CharField(
        primary_key=True,
        max_length=100,
    )
    stop_code = models.CharField(max_length=100)
    stop_name = models.CharField(max_length=200)
    stop_lat = models.FloatField()
    stop_long = models.FloatField()


class Stop_Times(models.Model):
    serial = models.AutoField(primary_key=True)
    trip_identifier = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    days = models.IntegerField(null=True)
    stop_identifier = models.CharField(max_length=100)


class Routes(models.Model):
    route_id = models.CharField(primary_key=True, max_length=100)
    route_name = models.CharField(max_length=50)


class Trips(models.Model):
    route_id = models.CharField(max_length=50)
    trip_id = models.CharField(primary_key=True, max_length=100)
    trip_headsign = models.CharField(max_length=200)
