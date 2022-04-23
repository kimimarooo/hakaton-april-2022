import folium
import geocoder

g = geocoder.ip('me')
print(g.latlng)

data = [[55.0234, 46.3745, [1, 2]], [47.5319, 53.2488, [1, 2]]]

print(data[0])
map = folium.Map(location=g.latlng, zoom_start=15)

for i in range(len(data)):
    folium.Marker(location=[data[i][0], data[i][1]], popup="Футбол", icon=folium.Icon(color='green')).add_to(map)
folium.Marker(location=g.latlng, popup="Вы", icon=folium.Icon(color='gray')).add_to(map)
map.save("map1.html")

from gps import *

def getPositionData(gps):
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        print ("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
