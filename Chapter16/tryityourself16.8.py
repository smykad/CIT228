import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

"""
for key in colors.PLOTLY_SCALES.keys():
    print(key)
"""

filename = 'Chapter16/data/all_hour.json'

# Explore the structure of the data
with open(filename) as f:
    # Earthquake data
    all_eq_data = json.load(f)

"""
# create the file and write the data to it
readable_file = 'Chapter16/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
"""

# After looking at the data we see that there is a key features correlating to all the dictionaries
all_eq_dicts = all_eq_data['features']

# print(len(all_eq_dicts)) # This determines that there is 158 dictionaries stored

mags, lons, lats, hover_texts = [], [], [], [] # create a list to store magnitude, longitudes and langitudes of the earthquakes
# Add in hover texts to give information

# Looking at the data magnitude is listed as the key mag under the key properties

for eq_dict in all_eq_dicts:
    
    # This retrieves the key mag that's nested inside the key properties to get the value of mag
    mag = eq_dict['properties']['mag']
    
    # we retrieve the key coordinates nested inside the key geometry in order to retrieve the longitude, which is stored as the first value
    lon = eq_dict['geometry']['coordinates'][0]
    
    # we retrieve the key coordinates nested inside the key geometry in order to retrieve the latitude, which is stored as the second value
    lat = eq_dict['geometry']['coordinates'][1]
    
    # Pull information to get the title from the json data
    title = eq_dict['properties']['title']
    
    # We are appending all the magnitudes into a list
    mags.append(mag)
    # Append longitudes
    lons.append(lon)
    # Append Latitudes
    lats.append(lat)
    # APpend hovertext
    hover_texts.append(title)
"""
print(mags[:10]) # Printing a list of magnitueds for the first 10 earthquakes in the list
print(lons[:5]) # Print the first 5 longitudes
print(lats[:5]) # Print the first 5 latitudes
"""

# Map the earthquakes
# data = [Scattergeo(lon = lons, lat = lats)] # Scattergeo chart allows you to overlay a scatter plot of geographic data on a map

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    # customize marker size
    'marker': {
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale': 'plasma',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes') # Give the chart a title

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='global_earthquakes.html')