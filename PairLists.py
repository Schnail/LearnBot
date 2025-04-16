import random
abclist = [["a",15],["c",2],["b",1],["e",5],["d",7]]

def bsortPairList(list):
    sortinglist = list
    sorted = False
    while sorted is False:
        i = checkSorted(sortinglist)
        if i == -1:
            sorted = True
        else:
            x = sortinglist[i]
            y = sortinglist[i +1]
            sortinglist[i] = y
            sortinglist[i + 1] = x
            
    return sortinglist   
               
def checkSorted(list):
    for x in range(0, len(list)-1):
        if list[x][1] < list[x + 1][1]:
            return x
    return -1

def makePairList(list1, list2):
    if len(list1) is not len(list2):
        ValueError("input lists have different lenghts")
        
    pairlist = []
        
    for x in range(0, len(list1)):
        pairlist.append([list1[x], list2[x]])
        
    return pairlist
    
def seperatePairList(pairlist):
    list1 = []
    list2 = []
    for x in pairlist:
        list1.append(x[0])
        list2.append(x[1])
    return [list1, list2]

def giveIndexOfElement(list, element): #needed to find position of specific elements e.g. "ru" to increase/decrease weighting
    
    i = 0
    for x in list:
        if x[0] == element:
            print(f"giveIndexOfElement found Element '{element}' at {i}")
            return i
        i = i + 1

    return None

def getTotalWeight(list):
    total = 0
    for x in list:
        total = total + x[1]
    print(f"getTotalWeight calculated total weight for {total}")
    return total

def pickWeightedRandom(list, totalweight):
    i = 0
    element = list[i]
    threshold  = random.randrange(0, totalweight)
    
    while totalweight > threshold:
        element = list[i]
        totalweight = totalweight - element[1]
        i = i + 1
    print(f"pickWeightedRandom picked {element}")
    return element

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
        
          

#--------------------------------------------

"""print("default:", abclist)
abclist2 = seperatePairList(abclist)
print("seperated:", abclist2[0],abclist2[1])
abclist3 = makePairList(abclist2[0],abclist2[1])
print("merged:", abclist3)
print("sorted:", bsortPairList(abclist))"""