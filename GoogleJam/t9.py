
def buildDictionary():
    s = {}
    count = 0
    start = '2'
    mod = 3
    num = lambda x, mod, count: x*((count%mod)+1)
    change = lambda count, mod: (chr(ord(start)+1),0) if count == mod-1 else (start,count+1)
    for i in range(26):
        if start == '7' or start == '9':
            s[chr(ord('a') + i)] = num(start, 4, count)
            start, count = change(count, 4)
        else:
            s[chr(ord('a') + i)] = num(start, 3, count)
            start, count = change(count, 3)

    # space
    s[' '] = '0'
    return s

def main():
    t9 = buildDictionary()
    print t9
    f = open('C-large-practice.in', 'r')
    lines = f.readlines()[1:]
    f.close()
    f = open('output_large.txt', 'w')
    case = 1
    for l in lines:
        num = 'Case #' + str(case) + ": "
        for c in l:
            if c == '\n':
                continue
            buf = t9[c]
            if num[-1] == buf[0]:
                num += ' ' + buf
            else:
                num += buf
        case += 1
        f.write(num+'\n')
    f.close()

main()