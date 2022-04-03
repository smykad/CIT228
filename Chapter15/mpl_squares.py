import matplotlib.pyplot as plt

# Method for stylizing and drawing a figure
def myStyle(title, x, y, myTitleFontSize, 
            myFontSizeX, myFontSizeY, myStyle, 
            myAxis, myWhich, myLabel, myColor,
            myScatterXValues, myScatterYValues, 
            myScatterSValue, myRange):
    # Sets the style of the figure
    # you can use print(plt.style.available) to see the different styles
    plt.style.use(myStyle)
    # fig represents the entire figure or collection of plots that are generated
    # the variable ax represents a single plot in the figure
    fig, ax = plt.subplots()
    # X values, Y values, Color, Size of plot point
    ax.scatter(myScatterXValues, myScatterYValues, cmap=myColor, s=myScatterSValue)
    # Set Chart title and label the axis
    ax.set_title(title, fontsize=myTitleFontSize)
    ax.set_xlabel(x, fontsize=myFontSizeX)
    ax.set_ylabel(y, fontsize=myFontSizeY)
    # Set size of tick labels
    ax.tick_params(axis=myAxis, which=myWhich, labelsize=myLabel)
    ax.axis(myRange)
    # use this if you want to save a png of the data plot
    # plt.savefig('square_plot.png', bbox_inches='tight')
    # shows the figure
    plt.show()
    
    # Method figure that takes x, y coordinates, plot point size and range
def myScatter(x,y,s,r):
    
    # Passes the variables to the styling method that also creates the figure
    myStyle('Cube Numbers', 'Value', 
            'Cube of Value', 24, 14, 14, 
            'seaborn', 'both', 'major', 
            14, plt.cm.Blues, x,y,s,r)
    
    
# Try it yourself 15-1 

# Numbers 1 through 5
x_val = [1,2,3,4,5]
# iterate through numbers 1 through 5 and cube it
y_val = [x**3 for x in x_val]
# set range for the table, 
# chose slightly above the values so they plot on figure nicely
r_val = [0, 5.1, 0, 5.1**3]

"""
    *************************
    *     Hands on 15-1     *
    *************************
"""
myScatter(x_val, y_val, 10, r_val)

# Try it yourself 15-2
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
r_values = [0, 5100, 0, 5100**3]

"""
    *************************
    *     Hands on 15-2     *
    *************************
"""
myScatter(x_values, y_values, 100, r_values)



