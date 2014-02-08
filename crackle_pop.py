#!/usr/bin/env python

def cracklepop(n):
    result = ''
    
    if n%3 == 0:
        result += 'Crackle'

    if n%5 == 0:
        result += 'Pop'

    if not result:
        result = str(n)

    return result

def main():
    for n in xrange(0, 101):
        print cracklepop(n)
    

if __name__ == '__main__':
    main()