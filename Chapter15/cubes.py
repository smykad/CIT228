# Hands on 1, 2, 3 and 4
# Doug Smyka
# CIT 228
# 4/3/2022

import matplotlib.pyplot as plt

# To see styles plt.style.available
"""
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

# set style
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
# Line Width
ax.plot(input_values, squares, linewidth=3)
# Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()
"""

# method for stylizing data
def myStyle(title, x, y, myTitleFontSize, 
            myFontSizeX, myFontSizeY, myStyle, 
            myAxis, myWhich, myLabel, myColor,
            myScatterXValues, myScatterYValues, 
            myScatterSValue, myRange):
    plt.style.use(myStyle)
    fig, ax = plt.subplots()
    ax.scatter(myScatterXValues, myScatterYValues, cmap=myColor, s=myScatterSValue)
    ax.set_title(title, fontsize=myTitleFontSize)
    ax.set_xlabel(x, fontsize=myFontSizeX)
    ax.set_ylabel(y, fontsize=myFontSizeY)
    ax.tick_params(axis=myAxis, which=myWhich, labelsize=myLabel)
    ax.axis(myRange)
    plt.show()
    
    # Method for stylized data that takes x,y, size and range values
def myScatter(x,y,s,r):
    myStyle('Cube Numbers', 'Value', 
            'Cube of Value', 24, 14, 14, 
            'seaborn', 'both', 'major', 14, plt.cm.Blues, x,y,s,r)
    
    
# Try it yourself 15-1
x_val = [1,2,3,4,5]
y_val = [x**3 for x in x_val]
r_val = [0, 5.5, 0, 130]

myScatter(x_val, y_val, 100, r_val)

# Try it yourself 15-2
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
r_values = [0, 5100, 0, 5100**3]

myScatter(x_values, y_values, 100, r_values)



