# Insertion Sort

def insertionSort(n):
    for i in range(len(n)):
        val = n[i]
        for x in range(i+1, len(n)):
            if val > n[x]:
                tmp = n[x]
                n[x] = val
                n[i] = tmp
                break
    return n
                
n = [3, 4, 1, 9, 0]

print n

print insertionSort(n)

# Binary Search
def binarySearch(n, value):
    
    low = 0
    high = len(n)
    while low < high:
        mid = (high+low)/2
        if n[mid] == value:
            return mid
        if n[mid] < value:
            low = mid+1
        else:
            high = mid
    return -1

n = [1,2,5,7,8,10,13]

print binarySearch(n, 8)

# Quick Sort with linear memory
def quicksort(n):
    if len(n) <= 1:
        return n 
    
    pivot = n[len(n)/2]
    n.remove(pivot)
    lesser = []
    greater = []
    
    for i in n:
        print i
        if i <= pivot:
            lesser.append(i)
        else:
            greater.append(i)
    
    print " "
    
    return quicksort(lesser) + [pivot] + quicksort(greater)

n = [3,1,5,7,5,6,2,13,2,5,6,7]

print quicksort(n)
    
    
# Quicksort in-place
def quicksortInPlace(n):
    pass

# MergeSort
def mergeSort(n):
    #Split the list
    if len(n) <= 1:
        return n
    
    middle = len(n)/2
    left = n[0:middle]
    right = n[middle:len(n)]
    
    # Divide further
    left = mergeSort(left)
    right = mergeSort(right)
    
    
    return merge(left, right)

def merge(left, right):
    result = []
    while True:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.remove(left[0])
            else:
                result.append(right[0])
                right.remove(right[0])
        elif len(left) == 0:
            return result + right
        elif len(right) == 0:
            return result + left
        
n = [3,4,1,6,87,3,4,62,3,1]

print mergeSort(n)
    
    
