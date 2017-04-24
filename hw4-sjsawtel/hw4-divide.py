#!/usr/bin/env python3

#file: hw4-divide.py
#Steven Sawtelle

#program establishes a given number of matrices of a given size and searches
#for a given key value in each matrix recursively in O(logn) time

import math, sys

def search(m, lowr, lowc, highr, highc, key):
    #print(m, lowr, lowc, highr, highc, key)
    if lowr > highr or lowc > highc:
        return -1, -1
    #get mids
    midr=int(math.ceil((lowr+highr)/2))
    midc=int(math.ceil((lowc+highc)/2))
    #base if number is in matrix
    if key == m[midr][midc]:
        return midr, midc
    #if too small round
    if key < m[midr][midc]:
        #call on the two matrixes that make up the rest
        (foundr, foundc) = search(m, lowr, lowc, midr-1, highc, key)
        if foundr == -1 or foundc == -1:
            return search(m, midr, lowc, highr, midc-1, key)
        return foundr, foundc
    #if too large round
    else:
        # call on the two matrixes that make up the rest
        (foundr, foundc) = search(m, lowr, midc+1, highr, highc, key)
        if foundr == -1 or foundc == -1:
            return search(m, midr+1, lowc, highr, highc, key)
        return foundr, foundc

def main():
    # get input
    content = []
    # take in num of test cases
    size = int(sys.stdin.readline())
    # value to search for(will be filled in later)
    key = 0
    for x in range(0, size):
        pair = sys.stdin.readline()
        content.append([int(y) for y in pair.split() if y.isdigit()])
        # get size n x n of matrix
        n = content[0][0]
        # fill in key value to search for
        key = content[0][1]
        # set up vars
        M = []
        count = 0
        #fill in matrix
        while count<n:
            templist = sys.stdin.readline()
            templist = [int(y) for y in templist.split()]
            M.append(templist)
            count+=1
        # search for key in matrix
        (resultr, resultc) = search(M, 0,0,len(M)-1,len(M)-1,key)
        if resultr == -1:
            print(str(key)+" - -")
        else:
            print(str(key) + " " + str(resultr) + " " + str(resultc))
        M=[]
        content=[]

if __name__ == "__main__":
    main()