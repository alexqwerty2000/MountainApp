import folium
import pandas

data = pandas.read_csv("Peak.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])
height = list(data["Height"])

map = folium.Map(location = [50.24, 30.27], zoom_start= 6, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "My group")

for lt,ln,pname,h in zip(lat,lon,name, height):
    fg.add_child(folium.Marker(location = [lt, ln], popup = pname+' '+str(h)+' m', icon = folium.Icon("green")))
map.add_child(fg)
map.save("Map.html")