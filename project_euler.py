import math
"""
Problem 1
"""
def sumOf5and3(n):
    sum = 0

    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            sum += i

    print "sum of %s with multipler 5 and 3 is %s." % (n, sum)

#sumOf5and3(1000)

"""
Problem 2
"""

def sumOfEvenFib(limit):
    if limit < 2:
        return 1
    
    fib1 = 1
    fib2 = 1
    result = 0
    sumEven = 0
    while result < limit:
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result

        if result%2 == 0 and result < limit:
            sumEven += result

    print "sum of even fib for %s is %s" % (limit, sumEven)

#sumOfEvenFib(4000000)

"""
Problem 3
"""

def checkPrime(n):
    """
    I feel like this can be written better with dynamic programming
    """
    if n < 2:
        return False

    sqrt = int(math.sqrt(n))

    for i in xrange(2,sqrt+1):
        if n%i == 0:
            return False
    return True

def largestPrimeFactor(n):

    for i in xrange(int(math.sqrt(n)),-1,-1):
        if n%i == 0:
            if checkPrime(i):
                return i

#print largestPrimeFactor(600851475143)

"""
Problem 4
"""
def isNumPaladrome(n):
    stringN = str(n)
    start = 0
    end = len(stringN)-1
    while end > start:
        if stringN[start] != stringN[end]:
            return False
        end -= 1
        start += 1
    return True

def findLargestPaladromeNum(digits):
    num1 = int('9'*digits)
    lowerBound = int('1'+'0'*(digits-1))
    maxPaladrome = 0
    while num1 >= lowerBound:
        num2 = num1
        while num2 >= lowerBound:
            product = num1 * num2
            if isNumPaladrome(product):
                if product > maxPaladrome:
                    maxPaladrome = product
            num2 -= 1
        num1 -= 1
    return maxPaladrome

#print findLargestPaladromeNum(3)

"""
Problem 5
"""
"""
This is very brute forcy... need to find a better way to do this
"""
def checkMultple(multiple, n):
    for i in multiple:
        if not n%i == 0:
            return False
    return True

def smallestMultiple(n):
    multiple = []
    for i in range(1,n+1):
        multiple.append(i)

    result = n
    while True:
        if checkMultple(multiple, result):
            return result
        result += n

#print smallestMultiple(20)

"""
Problem 6: Power Series
"""

def sumOfSquareDiff(n):
    n = float(n)
    sumSquares = n*(n+1)*(2*n+1)*(1/6.0)
    squareOfSums = (n*(n+1)*(0.5))**2

    print "Sum of Squares is %s" % sumSquares
    print "Square of Sums is %s" % squareOfSums
    print "Difference: %s" % (squareOfSums-sumSquares)

sumOfSquareDiff(100)

"""
Problem 7: Primes
"""
def crossOut(prime, l):
    for num in l:
        if num%prime == 0:
            l.remove(num)

def findPrime(placement):
    primes = [2]
    counter = placement
    primeIndex = 0
    l = range(3,counter,2)
    
    while len(primes) < placement:    
        while l:
            prime = primes[primeIndex]
            crossOut(prime, l)
            if primeIndex == len(primes)-1:
                primes.append(l[0])
                l.remove(l[0])
            primeIndex += 1
        primeIndex = 0
        if counter%2 == 0:
            l = range(counter-1, (counter+counter)-1, 2)
        else:
            l = range(counter, (counter+counter)-1, 2)
        counter = (counter+counter)-1
    print primes[placement-1]


#findPrime(10001)

"""
Problem 8
"""
import Queue

num = """73167176531330624919225119674426574742355349194934 
         96983520312774506326239578318016984801869478851843 
         85861560789112949495459501737958331952853208805511 
         12540698747158523863050715693290963295227443043557 
         66896648950445244523161731856403098711121722383113 
         62229893423380308135336276614282806444486645238749 
         30358907296290491560440772390713810515859307960866 
         0172427121883998797908792274921901699720888093776 
         65727333001053367881220235421809751254540594752243 
         52584907711670556013604839586446706324415722155397 
         53697817977846174064955149290862569321978468622482 
         83972241375657056057490261407972968652414535100474 
         82166370484403199890008895243450658541227588666881 
         16427171479924442928230863465674813919123162824586 
         17866458359124566529476545682848912883142607690042 
         4219022671055626321111109370544217506941658960408 
         07198403850962455444362981230987879927244284909188 
         84580156166097919133875499200524063689912560717606 
         05886116467109405077541002256983155200055935729725 
         71636269561882670428252483600823257530420752963450""".replace('\n', '').replace(' ', '')


def findGreatestProduct5(num):

    greatestProduct = 0
    product = 1
    q = Queue.Queue(5)
    for i in num:
        i = int(i)
        if q.full():
            if greatestProduct < product:
                greatestProduct = product
            remove = q.get()
            product = product/remove

        if i == 0:
            q = Queue.Queue(5)
            product = 1
            continue
            
        product = product * i
        q.put(i)
    return greatestProduct

#print findGreatestProduct5(num)

"""
Problem 9: Pythagorean triplet
"""

def findSpeicalPythoagoreanTrip():

    for m in range(15):
        for n in range(m+1, 30):
            a = n*n-m*m
            b = 2*n*m
            c = n*n+m*m
            if (a+b+c) == 1000:
                print "a: %s b: %s c: %s" %(a,b,c)
                print "product: %s" % (a*b*c)
                break 

            if (a+b+c) > 1000:
                break

#findSpeicalPythoagoreanTrip()


"""
Problem 10: sumOfPrimes
"""
def crossOut2(prime, l):
    for num in l:
        if num%prime == 0:
            l.remove(num)

def findPrimeSum(n):
    primeSum = 2
    l = range(3,n,2)
    currentPrime = 2

    while l:
        crossOut2(currentPrime, l)
        currentPrime = l[0]
        l.remove(l[0])
        primeSum += currentPrime

    print primeSum

    

findPrimeSum(2000000)