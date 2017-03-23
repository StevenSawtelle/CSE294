#!/usr/bin/env python3

#program shall brute force find the posible magic square solutions for 3

import sys
import itertools
import copy

def main():
    n = int(input())
    s=[]
    #define mag const
    magic_const = n*(n*n + 1) // 2
    #create iterable to be used to create 2d array
    I = [x for x in range(1, n*n+1)]
    #get all permutations
    P = itertools.permutations(I)
    #allocate 2d array to be filled in
    M = [[x for x in range(0, n)] for t in range(0, n)]
    for p in P:
        i=0
        for row in range(0,n):
            for col in range(0,n):
                M[row][col] = p[i]
                i+=1
    		    #check constraints
                passt = check(M, magic_const)
                if passt:
                    tempo = copy.deepcopy(M)
                    if tempo not in s:
                        s.append(tempo)
    for it in s:
        print(it)

def check(array, mag):
    #i first had this called passy but then i realized what that looked like oops
    passt=True
    #if any condition is broken do not return true
    if(array[0][0]+array[0][1]+array[0][2] != mag):
        passt = False
    if(array[1][0]+array[1][1]+array[1][2] != mag):
        passt = False
    if(array[2][0]+array[2][1]+array[2][2] != mag):
        passt = False
    if(array[0][0]+array[1][0]+array[2][0] != mag):
        passt = False
    if(array[0][1]+array[1][1]+array[2][1] != mag):
        passt = False
    if(array[0][2]+array[1][2]+array[2][2] != mag):
        passt = False
    if(array[0][0]+array[1][1]+array[2][2] != mag):
        passt = False
    return passt

if __name__ == "__main__":
    main()