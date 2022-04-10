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

plt.scatter(years, meats, c='red',label="Meats")
plt.scatter(years, sugars, c='pink', label="Sugars")
plt.scatter(years, alcohols, c='blue', label="Alcohols")
plt.ylabel('Calories')
plt.xlabel('years')
plt.suptitle('Caloric intake Comparison')
plt.title('Blah')
plt.legend(loc='best', fontsize=8)
plt.grid()
plt.show()

# EOF