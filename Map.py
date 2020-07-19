import folium
import pandas

data = pandas.read_csv("volcanos.txt")

map = folium.Map(location = [41.1118011,-114.1110001], zoom_start = 5)
fg1 = folium.FeatureGroup(name = "Volcanoes Markers")

def getColor(hg):
    if hg > 2000:
        return "red"
    elif hg > 1500:
        return "orange"
    else:
        return "green"

for name, lt , ln, height in zip(data["NAME"], data["LAT"], data["LON"], data["ELEV"]):
    fg1.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = name + "\nHeight:" + str(height) + "m", 
                               fill_color = getColor(height), color = "grey", fill_opacity = 0.7))

fg2 = folium.FeatureGroup(name = "Population Polygons")

fg2.add_child(folium.GeoJson(data =  open("world.json", "r", encoding="utf-8-sig").read(), 
style_function = lambda x : {'fillColor':'green' if x["properties"]["POP2005"] <= 10000000 else 'orange' 
if x["properties"]["POP2005"] <= 20000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map.html")