def decrypt(n):
    """Dummy decrypt method for testing"""
    if n == 'aBc7D8E':
        return 123
    else:
        raise ValueError

def tryId(word):
    try:
        id = decrypt(word)
        return id
    except:
        return None

def findId(n):
    """
    Takes in a corrupted n and tries all possible combinations of upper/lower case
    letters till the method finds the id. If it can't find the id, returns None.
    Since a letter can be only two states, we can use binary numbers to determine 
    the state of the letter. This saves a lot in memory compared to the recursive 
    version. This is still O(2**n) but memory is 0(n).
    
    Method checks if the character is an alphabet, and stores it in a dictionary.
    Then it counts to 2**(length of dictionary keys). It converts the number to 
    binary. Then it iterates through each bit, where 1 means to change the 
    letter to upper case and 0 means change the letter lower case. After iterating
    through the binary number, it checks the decrypt method to see if is a valid id.
    Then increments to the next binary number.
    Parameters:
    n - the corrupted key
    """
    if type(n) != str:
        return None
    indexes = {}
    for i in xrange(len(n)):
        if n[i].isalpha():
            indexes[i] = n[i]
    size = len(indexes.keys())
    numPossible = 2**size
    wordBuilder = [i for i in n]
    
    for i in xrange(numPossible):
        binary = bin(i)
        # Get rid of '0b and add leading zeros'
        binary = binary[2:]
        binary = '0'*(size-len(binary)) + binary
        for key in indexes.keys():
            if binary[counter] == '1':
                wordBuilder[key] = indexes[key].upper()
            else:
                wordBuilder[key] = indexes[key].lower()
        id = tryId(''.join(wordBuilder))
        if id:
            return id
    return None

n = 'abc7d8e'
id = findId(n)
print id

n = ''
id = findId(n)
print id

n = '1'
id = findId(n)
print id

n = 1
id = findId(n)
print id

n = -1
id = findId(n)
print id

n = None
id = findId(n)
print id