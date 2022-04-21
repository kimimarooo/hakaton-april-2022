import folium
import geocoder
g = geocoder.ip('me')
print(g.latlng)

map = folium.Map(location=g.latlng, zoom_start=15)

folium.Marker(location=g.latlng, popup="asdas", icon=folium.Icon(color='gray')).add_to(map)
for coordinates in [[50.5614, 46.0388], [50.5614, 49.0388]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color='green')).add_to(map)
map.save("map1.html")
