import csv 
import matplotlib.pyplot as plt
import numpy as np

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


def dictOfLists(myInt):
    ret = {}
    for x in range(1, myInt+1):
        ret["ret{0}".format(x)] = [x, x, x]
    return ret
    
def createList(myDict, myInt):
    ret = list(myDict.values())
    ret = ret[myInt]
    return ret

def createMultiList(myInt):
    myDict = dictOfLists(myInt)
    match myInt:
        case 1:
            ret1 = createList(myDict, 0)
            return ret1
        case 2:
            ret1 = createList(myDict, 0)
            ret2 = createList(myDict, 1)
            return ret1, ret2
        case 3:
            ret1 = createList(myDict, 0)
            ret2 = createList(myDict, 1)
            ret3 = createList(myDict, 2)
            return ret1, ret2, ret3
        case 4:
            ret1 = createList(myDict, 0)
            ret2 = createList(myDict, 1)
            ret3 = createList(myDict, 2)
            ret4 = createList(myDict, 3)
            return ret1, ret2, ret3, ret4



myFile = 'data_project/data/diet_data.csv'

with open(myFile) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)