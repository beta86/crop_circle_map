import folium 
import pandas

data = pandas.read_csv("crop_circles.txt")
lon = list(data["Lon"])
lat = list(data["Lat"])
crop = list(data["Crop"])

#Changes colour of markers depending on what type of crop.
def crop_colors(crop_type):
    if crop_type == "Wheat":
        return "blue"
    elif crop_type == "Maize":
        return "red"
    elif crop_type == "Barley":
        return "green"
    else:
        return "orange"

map=folium.Map(location=[51.5889385, -2.1049307], zoom_start=9, tiles="stamen Terrain")

#Creates a feature group for the crop circles and their locations.
fgc = folium.FeatureGroup(name="Crop_Circles")

for ln, lt, cr in zip(lon, lat, crop):
    fgc.add_child(folium.CircleMarker(location=[ln, lt], radius = 6, popup=cr, 
    fill_color=crop_colors(cr), color = "grey", fill_opacity=0.7))

'''
Creates a feature group for World population, 
this is represented by different colours depending on density of population
'''
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] <20000000 else "red"}))

#Calls to each feature group and adds the ability to switch on and off each group
map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("malmesbury.html")