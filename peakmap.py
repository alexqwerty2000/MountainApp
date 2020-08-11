import folium
import requests
from bs4 import BeautifulSoup

r = requests.get('https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%80%D1%88%D0%B8%D0%BD%D1%8B_%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D1%85_%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82')
content = r.content
soup = BeautifulSoup(content,'html.parser')
all = soup.find_all('tr')
peaks = all[1:]

def peak_color(h_peak):
    if h_peak < 1500:
        return "green"
    elif 1500<= h_peak < 2000:
        return "orange"
    else:
        return "red"
    
def transform_coordinates(coord):
    transorm_coord = coord[]
    return transform_coord

map = folium.Map(location = [48.54, 23.99], zoom_start= 8, tiles = "Stamen Terrain")
fgp = folium.FeatureGroup(name = "Mountaine Peak")

for item in peaks:
    peak = item.find_all('td')
    pname = peak[0].text
    h = float(peak[1].text)
    situated = peak[2].text
    coordinates = peak[3].text
    lt = round(float(coordinates[:2]) + float(coordinates[3:5])/60 + float(coordinates[6:8])/3600, 2)
    ln = round(float(coordinates[16:18]) + float(coordinates[19:21])/60 + float(coordinates[22:24])/3600, 2)
    # print()
    fgp.add_child(folium.CircleMarker(location = [lt, ln], popup = pname+' '+str(h)+' m', 
    radius = 3, fill_color = peak_color(h), color = "black", fill_opacity =0.7
    ))

fgl = folium.FeatureGroup(name='Mountain Lakes')
map.add_child(fgp)
map.add_child(fgl)
map.add_child(folium.LayerControl())
map.save("Map.html")
