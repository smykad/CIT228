import csv

from matplotlib import pyplot as plt

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

# food calories are kilocalories

# 0 United States
# 1 USA 


myFile = 'data_project/data/diet_data.csv'

with open(myFile) as f:
    reader = csv.reader(f)

    years, codes, sugars, alcohols = [], [], [], []

    for row in reader:
        match row[1]:
            case 'USA':
                year = int(row[2])
                code = row[1]
                sugar = row[4]
                alcohol = row[12]
                years.append(year)
                codes.append(code)
                sugars.append(sugar)
                alcohols.append(alcohol)

print(codes[:5], end=', ')
print()
print(years[:5], end=', ')
print()
print(sugars[:5], end=', ')
print()
print(alcohols[:5], end=', ')
