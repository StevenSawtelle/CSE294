#!/usr/bin/env python3

#name: Steven Sawtelle
#CSE 294
#started: 5-4-17

"""
view the source definition of this problem: Tidy Numbers at:
https://code.google.com/codejam/contest/3264486/dashboard#s=p1

this program shall take in a given amount of numbers, and then
for that many numbers determine if it is "tidy" - that is,
if the numbers from left to right are (not strictly) increasing
ie)
129 is tidy
132 is not tidy
"""

import sys

def checkTidy(lst):
	for x in range(0, len(lst)-1):
		if lst[x] > lst[x+1]:
			return False
	return True

def continuousLoop(splitVals):
	#key is that if a number is less than a number to its right, you need
	#to decrement that number and change all to the right to 9
	#this does not always work so the new number should be checked to make
	#sure it now fulfills "tidiness". otherwise keep doing it
	while not checkTidy(splitVals):
		for x in range(len(splitVals)-1):
			if splitVals[x] > splitVals[x+1]:
				splitVals[x] = splitVals[x] - 1
				for y in range(x+1,len(splitVals)):
					splitVals[y] = 9

def makeTidy(n):
	#funcion shall check if a number is "tidy" , ie) increasing
	#integers when read individually from left to right
	splitVals = []
	while n > 0:
		currentVal = n % 10
		splitVals.append(currentVal)
		n = n // 10
	#now have all digits in splitVals, flip it for easy use
	splitVals = splitVals[::-1]
	continuousLoop(splitVals)
	#reconstruct num
	base = 1
	splitVals = splitVals[::-1]
	tidynum = 0
	for x in range(len(splitVals)):
		tidynum += base * splitVals[x]
		base *= 10
	return tidynum

def main():
	#driver for this file, get size, then get that many inputs and process them
	inputSize = int(sys.stdin.readline())
	#have number of numbers to test, now start that testing process
	for x in range(1, inputSize+1):
		currentNum = int(sys.stdin.readline())
		tidynum = makeTidy(currentNum)
		print("Case #" + str(x) + ": " + str(tidynum))

#never forget this lil dude!
if __name__ == "__main__":
    main()