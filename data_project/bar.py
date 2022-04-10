import csv 
import matplotlib.pyplot as plt
import numpy as np

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

N = -4

meats = meats[N:]
sugars = sugars[N:]
alcohols = alcohols[N:]
years = years[N:] 

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]
barWidth=.25

#position of bar on x axis
br1 = np.arange(len(years)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

plt.xticks([r + barWidth for r in range(len(meats))],years) 

# creating the bar plot 
plt.bar(br1, meats, color ='lightgreen', width=barWidth, label="Meat") 
plt.bar(br2, sugars, color="pink",  width=barWidth, label="Sugar")
plt.bar(br3, alcohols, color="lightblue", width=barWidth,  label="Alcohol")
  
plt.ylabel("Kilocalories") 
plt.xlabel(f"{years[0]} - {years[-1]}") 
plt.title("Fast Food Consumption Per Day", c="lightblue", fontsize=18) 
plt.legend(loc="best")
plt.show()

#EOF