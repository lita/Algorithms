"""
iterate through words till it exceeds len(L):
remove last word. if len(L) > len(words) then 
create the difference to spaces. Iterate through
spaces (every odd index) and add one till no more 
spaces.

append that to the master list and repeat

if last line or len(words) == 1, we need ot left justifiy.
append the word and append spaces len(L) - len(words)
"""

def distributeSpaces(words, spaces):
    numEachSpaces = (2/spaces)
    for i in range(1,len(words)-2,2):
        words[i] = words[i] + numEachSpaces*' '

def justifityLeft(words, spaces):
    return words + " "*spaces

def textJustified(words, L):
    master = []
    cur = []
    counter = L
    for i in range(0,len(words)-1):
        word = words[i]
        if len(word) <= counter:
            cur.append(word)
            cur.append(' ')
            # need to account for the space
            counter = counter - (len(word)+1)
        else:
            spaces = counter
            del cur[-1]
            if len(cur) > 1:
                distributeSpaces(cur, spaces+1)
                
            else:
                cur = justifyLeft(cur, spaces)
                
            master.append(''.join(cur))
            cur = [word, ' ']
            print cur
            counter = L - (len(word)+1)
            print counter
    
    lastWord = words[-1]
    justifityLeft(lastWord, L-len(lastWord[0]))
    master.append(lastWord)
    
    return master


words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16

print textJustified(words,L)