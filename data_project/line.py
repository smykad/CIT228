import csv
import matplotlib.pyplot as plt

myFile = 'data_project/data/diet_data.csv'

with open(myFile) as f:
    reader = csv.reader(f)

    years, meats, sugars, alcohols = [], [], [], []

    for row in reader:
        match row[1]:
            case 'USA':
                year = row[2]
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


myFont = 'Comic Sans MS'

ax1 = plt.subplot(1,3,1)
ax1.plot(years,meats, marker='<', ls='--', c="purple")
plt.title("Meats", c="blue", fontfamily=myFont, fontsize=18)
plt.ylabel("Values Cubed", c="red", fontfamily=myFont, fontsize=14)
plt.xlabel("Year", c="yellow", fontfamily=myFont, fontsize=14)

ax2 = plt.subplot(1,3,2) 
ax2.plot(years,sugars, marker='o', ls=':', c="brown")
plt.style.use('seaborn')
plt.title("Sugars", c="blue", fontfamily=myFont, fontsize=18)
plt.ylabel("Values Squared", c="red", fontfamily=myFont, fontsize=14)
plt.xlabel("Input Values", c="yellow", fontfamily=myFont, fontsize=14)

ax3 = plt.subplot(1,3,3) 
ax3.plot(years,alcohols, marker='o', ls=':', c="brown")
plt.style.use('seaborn')
plt.title("Alcohols", c="blue", fontfamily=myFont, fontsize=18)
plt.ylabel("Values Squared", c="red", fontfamily=myFont, fontsize=14)
plt.xlabel("Input Values", c="yellow", fontfamily=myFont, fontsize=14)


plt.suptitle('Fun with Numbers', c="orange", fontfamily=myFont, fontsize=24)
plt.subplots_adjust(top=.8, wspace=.5)
plt.show()

# EOF