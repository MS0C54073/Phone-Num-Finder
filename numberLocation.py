from statistics import geometric_mean
import phonenumbers
from myNumber import number
from phonenumbers import geocoder
#from geocoder import geocode 
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

samNumber = phonenumbers.parse(number)
#ch_number = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(samNumber, "en")
#service_provider = phonenumbers.parse(number, "RO")
print(yourLocation)
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

Key = 'b930e9b25b384815bfeec458a20a3957'

geocoder = OpenCageGeocode(Key) 
query = str(yourLocation)
#results = geocoder.geocode(query)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

import folium
myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))

myMap.save("myLocation.html")




