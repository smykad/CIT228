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

l1,l2,l3,l4=createMultiList(4)

print(l1,l2,l3,l4)