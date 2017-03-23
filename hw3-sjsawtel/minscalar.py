#!/usr/bin/env python3

#program takes in n test cases and for each test case, takes in 2 vectors of m length.
#it shall return the minimum product of the permutations of the 2 vectors by brute force algorithm

import sys
import itertools

def process(x, y, size):
    #get permutations of each list
    Px = itertools.permutations(x)
    Py = itertools.permutations(y)
    #make min big because im lazy
    min = 999999999
    #loop through all iterations of each permutation to handle all cases
    for px in Px:
        #reget permutations for non-first loop
        Py = itertools.permutations(y)
        for py in Py:
            #check sum of products of both vectors
            product = 0
            for z in range(0, size):
                product += px[z] * py[z]
            if(product<min):
                min = product
    return min

def main():
    #get number of test cases
    n = int(input())
    #track which test case we are on
    count=1
    while(n>0):
        #get size of current vector
        size = int(input())
        #two vectors
        x=[]
        y=[]
        #fill in both vectors
        for i in range(0, size):
            x.append(int(input()))
        for i in range(0, size):
            y.append(int(input()))
        #get min for the two vectors
        min = process(x, y, size)
        #print output and handle increment/decrement
        print("Case #", count, ": ", str(min),sep="")
        count+=1
        n-=1

if __name__ == "__main__":
    main()