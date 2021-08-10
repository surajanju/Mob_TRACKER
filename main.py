import phonenumbers
from test import number

from phonenumbers import geocoder

key = 'Your Key From OpenCageGeocode'
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))
# for service Provider Detail
from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

# for geo-location of number

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(service_nmber)

results = geocoder.geocode(query)
print(results)

lati = results[0]['geometry']['lat'],

lngi = results[0]['geometry']['lng'],

print(lati, lngi)
