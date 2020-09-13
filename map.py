import folium 
import pandas

data = pandas.read_csv("crop_circles.txt")
lon = list(data["Lon"])
lat = list(data["Lat"])
crop = list(data["Crop"])


def crop_colors(crop_type):
    if crop_type == "Wheat":
        return "blue"
    else:
        return "orange"


map=folium.Map(location=[51.5889385, -2.1049307], zoom_start=6, tiles="stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for ln, lt, cr in zip(lon, lat, crop):
    fg.add_child(folium.Marker(location=[ln, lt], popup=cr, icon=folium.Icon(color=crop_colors(cr))))
# git testing
# test 2
map.add_child(fg)

map.save("malmesbury.html")