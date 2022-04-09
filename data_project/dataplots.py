import csv

import plotly.graph_objects as go
from plotly import offline

# 0 Entity
# 1 Code
# 2 Year
# 3 Other (FAO (2017)) (kilocalories per person per day)
# 4 Sugar (FAO (2017)) (kilocalories per person per day)
# 5 Oils & Fats (FAO (2017)) (kilocalories per person per day)
# 6 Meat (FAO (2017)) (kilocalories per person per day)
# 7 Dairy & Eggs (FAO (2017)) (kilocalories per person per day)
# 8 Fruit and Vegetables (FAO (2017)) (kilocalories per person per day)
# 9 Starchy Roots (FAO (2017)) (kilocalories per person per day)
# 10 Pulses (FAO (2017)) (kilocalories per person per day)
# 11 Cereals and Grains (FAO (2017)) (kilocalories per person per day)
# 12 Alcoholic Beverages (FAO (2017)) (kilocalories per person per day)
# 0              1   2    3  4  5    6   7   8  9   10 11  12 
# United States,USA,1989,23,574,711,441,432,201,94,27,767,163
# food calories are kilocalories

# 0 United States
# 1 USA 


myFile = 'data_project/data/diet_data.csv'

with open(myFile) as f:
    reader = csv.reader(f)

    years, meats, sugars, alcohols = [], [], [], []

    for row in reader:
        match row[1]:
            case 'USA':
                year = int(row[2])
                meat = row[6]
                sugar = row[4]
                alcohol = row[12]
                years.append(year)
                meats.append(meat)
                sugars.append(sugar)
                alcohols.append(alcohol)
N = -3
years = years[N:]
meats = meats[N:]
sugars = sugars[N:]
alcohols = alcohols[N:]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=sugars,
    name='Sugar',
    marker_color='rgb(50, 205, 50)'
))
fig.add_trace(go.Bar(
    x=years,
    y=meats,
    name='Meat',
    marker_color='rgb(247, 7, 127)'
))
fig.add_trace(go.Bar(
    x=years,
    y=alcohols,
    name='Alcohol',
    marker_color='rgb(7, 87, 247)'
))

layout = fig.update_layout(
    title='Dietary composotions by commodity group, United States',
    title_font_color='darkblue',
    title_font_size=30,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Calories',
        titlefont_size=16,
        tickfont_size=14,
        
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig.show()

# offline.plot({'data': fig, 'layout':layout}, filename='plotly.html')


