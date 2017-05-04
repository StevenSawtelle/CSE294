#!/usr/bin/env python3

import sys
from queue import *

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

#simple little class that allows for using nodes as needed
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printOut(root):
    print("begin")
    #thisLevel will track current level of nodes
    thisLevel = [root]
    while thisLevel:
        nextLevel = []
        #print each element of thisLevel and add all of its
        #children to nextLevel
        for n in thisLevel:
            print((n.val), end = ' ')
            if n.left: nextLevel.append(n.left)
            if n.right: nextLevel.append(n.right)
        print()
        #update thisLevel to be the nextLevel
        thisLevel = nextLevel
        #will stop when nextLevel is empty then, which is good
    print("end")

def flip(root):
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    flip(root.left)
    flip(root.right)
    return root

def proceed(fullList):
    #set up for transferring from level order traversal to binary tree
    count = 0
    q = Queue()
    tempNode = TreeNode(fullList[0])
    root = tempNode
    q.put(tempNode)
    tempNode = None
    #basically for each node add the appropriate children then q the children
    #make sure not to actually add the -
    for x in range(1, len(fullList)):
        #create node for this index and add it to queue
        newTemp = TreeNode(fullList[x])
        q.put(newTemp)
        #first child
        if(count == 0):
            tempNode = q.get()
            count = 1
            tempNode.left = newTemp
        #second child
        else:
            count=0
            tempNode.right = newTemp

    #now our tree has been created
    root = flip(root)
    printOut(root)

def main():
    going = False
    fullList=[]
    #read all lines from stdin
    for line in sys.stdin:
        if not going:
            if line=="begin\n":
                going = True
                fullList=[]
        else:
            #check if we can go forward now
            if(line=="end\n"):
                going = False
                proceed(fullList)
            #get current line as list of integers or -'s
            else:
                for val in [x for x in line.split()]:
                    fullList.append(val)

#ever-present little driver
if __name__ == "__main__":
    main()