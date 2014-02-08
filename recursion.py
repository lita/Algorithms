def sumOfSets(n):
    if n == 2:
        return [[1,1]]
    if n == 1:
        return []
    newSets = []
    for i in range(1,n):
        diff = n-i
        prev = sumOfSets(diff)
        new = [i, diff]
        new.sort()
        newSets.append(new)
        for s in prev:
            cur = s+[i]
            cur.sort()
            if not cur in newSets:
                newSets.append(cur)
    return newSets
    
sets = sumOfSets(7)
print sets

print "Choices"

def _choices(n, i, path):
    if n is None or i >= len(n):
        print path
        return
    
    choices = n[i]
    
    for choice in choices:
        _choices(n, i+1, path+[choice])
    
def choices(n):
    """
    Given n sets of choices: (1,2,3), (2,3,4), (4,5) 
    You pick one element from each set of choicesself.
    Generate all possible picking.
    """
    _choices(n, 0, [])

n = [[1,2,3],[2,3,4],[4,5],[3]]

choices(n)

def outputStars(n):
    """
    Given a Tuple for eg. (a, b, c).. 
    Output : (*, *, *), (*, *, c), (*, b, *), (*, b, c), (a, *, *), (a, *, c), 
    (a, b, *), (a, b, c)
    """
    return _outputStars(n, 0)

def _outputStars(n, index):
    if index >= len(n):
        return [[]]
    
    sets = _outputStars(n, index+1)
    result = []
    for set in sets:
        #append on
        result.append(['*'] + set)
        result.append([n[index]] + set)
    
    return result

n = ['a','b','c']
print outputStars(n)

"""
Given the array of digits (0 is also allowed), what is the minimal sum of two 
integers that are made of the digits contained in the array. 
For example, array: 1 2 7 8 9. The min sum (129 + 78) should be 207
"""

def minSumArray(n):
    num1 = []
    num2 = []

    for i in range(len(n)):
        if i%2==0:
            num1.append(n[i])
        else:
            num2.append(n[i])
    print int(''.join(map(str, num1))) + int(''.join(map(str,num2)))

minSumArray([1,2,3,5,6,8])    

"""
Find all permutations of a string
"""

def stringPerm(a, start, end):
    if start == end-1:
        print ''.join(a)

    for i in range(start, end):
        tmp = a[start]
        a[start] = a[i]
        a[i] = tmp
        stringPerm(a, start+1, end)
        tmp = a[start]
        a[start] = a[i]
        a[i] = tmp


def stringPermStart(s):
    a = [x for x in s]
    stringPerm(a, 0, len(a))

stringPermStart('abc')