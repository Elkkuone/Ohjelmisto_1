
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test")

location = geolocator.geocode("175 5th Avenue NYC")

print(location.latitude,location.longitude)

"""

geolocator = Nominatim(user_agent="test")

location1 = geolocator.geocode(str(var1),timeout = 10)
location2 = geolocator.geocode(str(var2),timeout = 10)
print(location1)
print(location2)
print(location1.latitude,location1.longitude)
print(location2.latitude,location2.longitude)


"""