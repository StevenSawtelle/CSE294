#!/usr/bin/env python3

import sys

#file: bintree-flip.py
#Steven Sawtelle
"""
program will create a binary tree based on input in this format:
begin
8
4 6
1 6 3 5
end
begin
...
end
...
and for each begin - end combo create a binary tree.
Then it will flip the binary tree around the vertical axis
and print out the binary tree in a similar fashion
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def proceed(headNode):
    pass

def main():
    count=1
    going = False
    #read all lines from stdin
    for line in sys.stdin:
        if not going:
            if line=="begin\n":
                going = True
        else:
            #check if we can go forward now
            if(line=="end\n"):
                going = False
                #proceed(headNode)
            #get current line as list of integers or -'s
            temp = [x for x in line.split()]
            print((temp))
            #increment count
        count+=1


#ever-present little driver
if __name__ == "__main__":
    main()