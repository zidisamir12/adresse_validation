from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='babatundearemu22gmail.com')
location = geolocator.geocode('algerie wahran  bir el djir 11220  ')
print(location.address)