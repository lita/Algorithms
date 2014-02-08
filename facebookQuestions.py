import random
print "InPlace Quicksort"
def partition(array, start, end, pivotIndex):
    if not (start <= pivotIndex <= end):
        raise ValueError("Pivot is not valid")
    
    # Move the pivot to the beginning of the list
    array[start], array[pivotIndex] = array[pivotIndex], array[start]
    pivot = array[start]
    i = start+1
    j = start+1
    
    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    
    #place the pivot to the beginning of the greater than boarder
    array[start], array[i-1] = array[i-1], array[start]
    return i
    
def quicksort(n, start=0, end=None):
    if end == None:
        end = len(n)-1
    if end - start < 1:
        return
    
    pivotIndex = random.randint(start, end)
    i = partition(n, start, end, pivotIndex)
    quicksort(n, start, i-1)
    quicksort(n, i+1, end)
    

l = [3,2,69,21,50,100,23]

quicksort(l)
print l


"""
You are given an array of 1's 2's and 3's. Sort this list so the 1's are first,
the 2's come second, and the 3's come third. 

Ex: Input [1, 3, 3, 2, 1] 
Output [1, 1, 2, 3, 3] 

But there is a catch!! The algorithm must be one pass, which means no merge/quick 
sort. Also no extra list allocations are allowed, which means no 
bucket/radix/counting sorts. 

You are only permitted to swap elements.
"""
print "Dutch National Flag"
def dutchNationalFlag(n):
    begin = 0
    end = len(n)-1
    i=0
    while i < len(n)-1:
        if n[i] == 1:
            n[begin], n[i] = n[i], n[begin]
            begin += 1
            i += 1
            
        elif n[i] == 3 and i < end:
            n[end], n[i] = n[i], n[end]
            end -= 1
        else:
            i += 1

l = [1, 3, 3, 2, 1] 
dutchNationalFlag(l)
print l

print "Combinations"

"""
Given two integers n and k, return all possible combinations of 
k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
"""

def combos(n, k):
    return _combos(n, k, 1, [])

def _combos(n, k, minNum, used):
    if k == 0:
        return [[]]
    if k > n:
        raise ValueError('Cannot have k greater than n')
    
    results = []
    for i in range(minNum, n+1):
        if i in used:
            continue
        sums = _combos(n, k-1, i+1, used+[i])
        for sum in sums:                
            sum = [i] + sum
            results.append(sum)
    return results

print combos(4, 4)