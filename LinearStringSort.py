"""
Sort letters in a word in linear time.

Only works for lowercase. need to handle uppercase later
"""
def AlphabetSoup(str): 

  alphabet = [0]*26
  
  for ch in str:
    if not ch.isalpha():
      continue
    index = ord(ch.lower())-ord('a')
    alphabet[index] += 1
  
  word = []
  for i in xrange(len(alphabet)):
    if alphabet[i]:
      ch = chr(i+ord('a'))
      word.append(ch*alphabet[i])
  
  return ''.join(word)

print 'test'
print AlphabetSoup('hello')