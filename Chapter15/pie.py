import matplotlib.pyplot as plt

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numUsed = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)  
wedgeColors = ('lightgreen','orange','lightblue','lavender','pink')

fig1, ax1 = plt.subplots()

ax1.pie(numUsed, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=100, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Popular Graphic Formats on the web")

plt.show()