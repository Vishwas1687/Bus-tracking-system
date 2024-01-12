import csv
import os
from app.models import *


def run():
    file1 = open(
        "C:/Users/G Vishwas/Desktop/extracting_data/extracting_data/routes.csv"
    )
    file2 = open("C:/Users/G Vishwas/Desktop/extracting_data/extracting_data/trips.csv")
    file3 = open(
        "C:/Users/G Vishwas/Desktop/extracting_data/extracting_data/stop_times.csv"
    )
    file4 = open("C:/Users/G Vishwas/Desktop/extracting_data/extracting_data/stops.csv")
    routes_file = csv.reader(file1)
    trips_file = csv.reader(file2)
    stop_times_file = csv.reader(file3)
    stops_file = csv.reader(file4)

    count = 1

    Routes.objects.all().delete()
    Stop_Times.objects.all().delete()
    Stops.objects.all().delete()
    Trips.objects.all().delete()

    for record in routes_file:
        if count == 1:
            pass
        else:
            Routes.objects.create(
                route_id=record[0].strip(), route_name=record[1].strip()
            )
        count = count + 1

    count = 1

    for record in trips_file:
        if count == 1:
            pass
        else:
            Trips.objects.create(
                route_id=record[0].strip(),
                trip_id=record[1].strip(),
                trip_headsign=record[2].strip(),
            )
        count = count + 1

    count = 1

    for record in stop_times_file:
        if count == 1:
            pass
        else:
            arrival_time = record[1].strip()
            departure_time = record[2].strip()
            counter = 0
            days = 0
            if int(arrival_time[0:2]) >= 24:
                hours = int(arrival_time[0:2]) - 24
                minutes = arrival_time[3:5]
                seconds = arrival_time[6:8]
                if hours < 10:
                    hours = "0" + str(hours)
                else:
                    hours = str(hours)
                arrival_time = hours + ":" + minutes + ":" + seconds
                counter = 1
            if int(departure_time[0:2]) >= 24:
                hours = int(departure_time[0:2]) - 24
                minutes = departure_time[3:5]
                seconds = departure_time[6:8]
                if hours < 10:
                    hours = "0" + str(hours)
                else:
                    hours = str(hours)
                departure_time = hours + ":" + minutes + ":" + seconds
                counter = 2
            if counter == 1:
                days = 1
            Stop_Times.objects.create(
                trip_identifier=record[0].strip(),
                arrival_time=arrival_time,
                departure_time=departure_time,
                stop_identifier=record[3].strip(),
                days=days,
            )
        count = count + 1

    count = 1

    for record in stops_file:
        if count == 1:
            pass
        else:
            Stops.objects.create(
                stop_id=record[0].strip(),
                stop_code=record[1].strip(),
                stop_name=record[2].strip(),
                stop_lat=record[3].strip(),
                stop_long=record[4].strip(),
            )
        count = count + 1
