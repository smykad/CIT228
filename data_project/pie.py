import csv 
import matplotlib.pyplot as plt

myFile = 'data_project/data/diet_data.csv'

with open(myFile) as f:
    reader = csv.reader(f)

    years, meats, sugars, alcohols = [], [], [], []

    for row in reader:
        match row[1]:
            case 'USA':
                year = int(row[2])
                meat = int(row[6])
                sugar = int(row[4])
                alcohol = int(row[12])
                years.append(year)
                meats.append(meat)
                sugars.append(sugar)
                alcohols.append(alcohol)

N = -1
years = years[N:]
meats = meats[N:]
sugars = sugars[N:]
alcohols = alcohols[N:]             
                
labels = 'Burgers', 'Pancakes', 'Whiskey'
numUsed = [meats[0], sugars[0], alcohols[0]]
explode = (.1, 0, 0)  
wedgeColors = ('red','orange','brown')

fig1, ax1 = plt.subplots()

ax1.pie(numUsed, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=100, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle(f"Caloric intake by category in the United States {years[0]}")

plt.show()

# EOF