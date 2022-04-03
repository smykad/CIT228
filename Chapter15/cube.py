"""
********************************
Name: Doug Smyka
Class: CIT 228
Date: 4.3.2022
Assignment: Hands on 1,2,3 and 4
********************************
"""

import matplotlib.pyplot as plt


# Hands on 1, 2, 3

inputVal=range(1,6)
cubed = [v**3 for v in inputVal]
raised=[v**2 for v in inputVal]

myFont = 'Comic Sans MS'

ax1 = plt.subplot(1,2,1)
ax1.plot(inputVal,cubed, marker='<', ls='--', c="purple")
plt.title("Cubed Numbers", c="blue", fontfamily=myFont, fontsize=18)
plt.ylabel("Values Cubed", c="red", fontfamily=myFont, fontsize=14)
plt.xlabel("Input Values", c="yellow", fontfamily=myFont, fontsize=14)

ax2 = plt.subplot(1,2,2) 
ax2.plot(inputVal,raised, marker='o', ls=':', c="brown")
plt.style.use('seaborn')
plt.title("Squared Numbers", c="blue", fontfamily=myFont, fontsize=18)
plt.ylabel("Values Squared", c="red", fontfamily=myFont, fontsize=14)
plt.xlabel("Input Values", c="yellow", fontfamily=myFont, fontsize=14)

plt.suptitle('Fun with Numbers', c="orange", fontfamily=myFont, fontsize=24)
plt.subplots_adjust(top=.8, wspace=.5)
plt.show()

