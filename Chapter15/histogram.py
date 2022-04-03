import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#scores showing how many yards students ran in 12 minutes
# 1 mile = 1,760 yards
fitness_test=[2901,1760,3000,2824,3235,2050,2265,2500,2400,2625,3550,1850,1890,3200,2900,2975,3000,2220,2250]

myBins = len(pd.value_counts(np.array(fitness_test)))

# can replace myBins with 18, there's only one duplicate

plt.hist(fitness_test, bins=myBins, color='pink')
plt.ylabel('frequency')
plt.xlabel('recorded distance')
plt.suptitle('Yards ran in 12 minutes')

plt.show()







    


        

    
    
