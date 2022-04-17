import matplotlib.pyplot as plt
import numpy as np

# Information on USD to Sterling pound obtained from google search 4/16/2022

usd = [1]
pound = [1.31]

barWidth=.25

#position of bar on x axis
br1 = np.arange(len(usd)) 
br2 = [x + barWidth for x in br1]

plt.xticks([1],['money']) 

# creating the bar plot 
plt.bar(br1, usd, color ='orange', width=barWidth, label="USD") 
plt.bar(br2, pound, color="brown",  width=barWidth, label="Pound")
  
plt.ylabel("USD") 
plt.title("USD vs British Pound",  fontsize=18) 
plt.legend(loc="best")
plt.show()

#EOF