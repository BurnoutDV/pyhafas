import json
import datetime

from pyhafas import HafasClient
from pyhafas.profile.nasa import NASAProfile

client = HafasClient(NASAProfile())

print("Starting query for a place...")

first_location = client.locations("Leipzig, Völkerschlachtdenkmal")[0]
print(json.dumps(first_location.__dict__, indent=2))

second_location = client.locations("Leipzig, Hauptbahnhof")[0]
print(json.dumps(second_location.__dict__, indent=2))

departures = client.departures(
    station=first_location.id,
    date=datetime.datetime.now(),
    max_trips=2,
    products={
        'nationalExpress': True,
        'national': True,
        'regional': True,
        'suburban': True,
        'bus': True,
        'tram': True,
    }
)

# departures are not iterable, i was tempted to fix that, but no, this is out of scope

basic_departures = []
for boardleg in departures:
    one_depart = {}
    for k, v in boardleg.__dict__.items():
        if k == "station":
            one_depart[k] = v.__dict__
        elif k == "dateTime":
            one_depart[k] = v.isoformat()
        elif k == "delay":
            one_depart[k] = v.total_seconds()
        else:
            one_depart[k] = v
    basic_departures.append(one_depart)

print(json.dumps(basic_departures, indent=2))

journeys = client.journeys(
    origin=first_location,
    destination=second_location,
    date=datetime.datetime.now(),
    max_changes=2,
    min_change_time=15
)

basic_journey = []

for journey in journeys:
    one_journey = {}
    for k, v in journey.__dict__.items():
        if k == "legs":
            # this is getting too much for an example, cutting this now
            one_journey[k] = [str(f) for f in v]
        elif k == "date":
            one_journey[k] = v.isoformat()
        elif k == "duration":
            one_journey[k] = v.total_seconds()
        else:
            one_journey[k] = v
    basic_journey.append(one_journey)
print(json.dumps(basic_journey, indent=2))

