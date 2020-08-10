import folium
import pandas

data = pandas.read_csv("Peak.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])
height = list(data["Height"])

def peak_color(h_peak):
    if h_peak < 1000:
        return "green"
    elif 1000<= h_peak < 2025:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [48.54, 23.99], zoom_start= 8, tiles = "Stamen Terrain")
fgp = folium.FeatureGroup(name = "Mountaine Peak")

for lt,ln,pname,h in zip(lat,lon,name, height):
    fgp.add_child(folium.CircleMarker(location = [lt, ln], popup = pname+' '+str(h)+' m', 
    # icon = folium.Icon(color = peak_color(h))
    radius = 6, fill_color = peak_color(h), color = "black", fill_opacity =0.7
    ))

fgl = folium.FeatureGroup(name='Mountain Lakes')
map.add_child(fgp)
map.add_child(fgl)
map.add_child(folium.LayerControl())
map.save("Map.html")