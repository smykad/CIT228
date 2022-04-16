import csv 
import matplotlib.pyplot as plt

myFile = 'data_project/data/diet_data.csv'

with open(myFile) as f:
    reader = csv.reader(f)

    years, toasts, beans = [], [], []

    for row in reader:
        match row[1]:
            case 'GBR':
                year = int(row[2])
                toast = int(row[11])
                bean = int(row[9])
                years.append(year)
                toasts.append(toast)
                beans.append(bean)

N = -1
years = years[N:]
toasts = toasts[N:]
beans = beans[N:]             
                
labels = 'Toast', 'Beans'
numUsed = [toasts[0], beans[0]]
explode = (.2, 0)  
wedgeColors = ('orange','brown')

fig1, ax1 = plt.subplots()

ax1.pie(numUsed, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=10, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle(f"Beans n Toast United Kingdom {years[0]}")

plt.show()