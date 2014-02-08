#!/usr/bin/env python
# encoding: utf-8
import Queue

def convertBoard(n):
    board = []
    counter = 0
    for i in range(3):
        tmp  = []
        for j in range(3):
            tmp.append(n[counter])
            counter += 1
        board.append(tmp)

    return board
    

def convertNum(n):
    string = [x for sublist in n for x in sublist]
    return ''.join(string)

def turnOn(n, i, j):
    """
    Turn on north, south, west and east
    """
    #Turn on north
    if j+1 < len(n):
        n[i][j+1] = '0' if n[i][j+1] == '1' else '1'
    
    # Turn on south
    if j-1 >= 0:
        n[i][j-1] = '0' if n[i][j-1] == '1' else '1'
        
    #Turn on east
    if i+1 < len(n):
        n[i+1][j] = '0' if n[i+1][j] == '1' else '1'
    
    # Turn on west
    if i-1 >= 0:
        n[i-1][j] = '0' if n[i-1][j] == '1' else '1'
    
    n[i][j] = '0' if n[i][j] == '1' else '1'
    
    return convertNum(n)
    

def isWinningBoard(n):    
    if n == '000000000':
        return True
    else:
        return False

def lightsOut(n):
    if len(n) != 9:
        raise ValueError('Not a 3x3 board')
    queue = Queue.Queue()
    queue.put(n)
    moves = {}  #maps to board to moves
    
    while not queue.empty():
        curString = queue.get()
        if curString in moves:
            movePath = moves[curString]
        else:
            movePath = []
            
        for i in range(3):
            for j in range(3):
                curBoard = convertBoard(curString)
                if curBoard[i][j] == '1':
                    result = turnOn(curBoard, i, j)
                    if isWinningBoard(result):
                        return movePath + [(i,j)]
                    else:
                        queue.put(result)
                        if not result in moves:
                            moves[result] = movePath + [(i,j)]
    
    # Could not find solution
    return None 

def main():
    board = '010111010'
    result = lightsOut(board)
    print result
    

if __name__ == '__main__':
    main()

