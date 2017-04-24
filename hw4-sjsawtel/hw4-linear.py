#!/usr/bin/env python3

#file: hw4-linear.py
#Steven Sawtelle

#program establishes a given number of matrices of a given size and searches
#for a given key value in each matrix linearly (O(n) time)

import sys

def search(m, key):
    # function to linearly search a 2D matrix, line by line
    if len(m)<1:
        #handle null matrix
        return str(key) + " - -"
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            #check each element
            if m[i][j]==key:
                return str(key) + " " + str(i) + " " + str(j)
    return str(key) + " - -"

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
        result = search(M, key)
        sys.stdout.write(str(result)+"\n")
        M=[]
        content=[]

if __name__ == "__main__":
    main()