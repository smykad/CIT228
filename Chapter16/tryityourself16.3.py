import csv
from datetime import datetime

from matplotlib import pyplot as plt
# 0 STATION 1 NAME 2 DATE 3 TMAX 4 TMIN

myFile = 'Chapter16/data/SanFran2022.csv'
def myData(filename, myDateIndex, myHighIndex, myLowIndex):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Get dates and high temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[myDateIndex], '%Y-%m-%d') # Convert dates
            try:
                high = int(row[myHighIndex])
                low = int(row[myLowIndex])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                lows.append(low)
                highs.append(high)
        ret = dates, highs, lows
        return ret
    
dates, highs, lows = myData(myFile, 2,3,4)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2022\nSan Francisco, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # Draws date labels diagnoally to prevent overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()