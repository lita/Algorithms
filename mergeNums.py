import math
def findItem(L, num):
    middle = len(L)/2
    high = len(L)
    low = 0
    
    print num
    while high > low:
        start,end = L[middle]
        print "start: " + str(start)
        print "end: " + str(end)
        print "num: " + str(num)
        print ''
        if start <= num and num <= end:
            return middle
        if num < start:
            if middle-1 < 0:
                return middle
            elif L[middle-1][1] < num:
                return middle
        if num > end:
            if middle+1 >= len(L):
                return middle
            elif L[middle+1][0] > num:
                return middle
        if num > end:
            low = middle+1
            middle = (low+high)/2
        else:
            high = middle
            middle = (low+high)/2
        print "middle " + str(middle)
        
    return -1
    
def mergeNums(L, b):
    # Edge cases
    if b[1] < L[0][0]:
        return [b] + L
    if b[0] > L[-1][1]:
        return L + [b]
    start, end = b
    indexLower = findItem(L, b[0])
    if indexLower < -1:
        print "did not find lower"
        exit(1)
    if L[indexLower][0] > start:
        L[indexLower][0] = start
    indexUpper = findItem(L, b[1])
    if indexUpper < 0:
        print "did not find upper"
        exit(1)
    if end > L[indexUpper][1]:
        L[indexLower][1] = end
    else:
        L[indexLower][1] = L[indexUpper][1]
        
    return L[0:indexLower+1] + L[indexUpper+1:len(L)]

L = [[1,2],[4,5],[8,10]]
b = [9,20]
print mergeNums(L,b)