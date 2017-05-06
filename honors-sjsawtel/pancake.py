#!/usr/bin/env python3

#name: Steven Sawtelle
#CSE 294
#started: 5-4-17

"""
view the source definition of this problem: Oversized Pancake Flipper at:
https://code.google.com/codejam/contest/3264486/dashboard

this program shall take in a given amount of strings consisting of + and -,
and then for that many strings find the amount of flips needed (if possible)
on a griddle that can flip k pancakes at a time, where k is an integer <=
the length of the string. here, an example will make more sense:

1 <- read in 1 test case for this execution
---+-++- 3 <- the first part is a vizualization, and we want all of them to be 
				'+'. the girddle can flip 3 characters to the other at a time, and
				must flip 3
output: Case #1: 3

explanation:
start: ---+-++-
first flip: ++++-++- <- first index 0-2 flipped
second flip: +++++--- <- from index 4-6 flipped 
third flip: ++++++++ <- from index 5-7 flipped

so the output is number of flips: 3
"""

import sys

def doAPass(inputstring, inputnum):
	#function to flip a string once with inputnum elements being flipped
	newstring = ""
	x=0
	flipped = False
	#for (almost) each element 
	while x < len(inputstring)-inputnum+1:
		#if it is a - and this cycle has not seen a griddle flip already
		if(inputstring[x]=='-') and not flipped:
			#flip the next inputnum chars
			for y in range(x, x+inputnum):
				if inputstring[y]=='-':
					newstring+='+'
				else:
					newstring+='-'
			#also adjust sentinels accordingly
			x+=inputnum
			flipped = True
		else:
			#otherwise just add the current character
			newstring+=inputstring[x]
			x+=1
	#fill in the rest of the string before returning
	leng = len(newstring)
	diff = len(inputstring)-leng
	if diff != 0:
		for y in range(0, diff):
			newstring += inputstring[leng+y]
	return newstring

def flip(inputstring, inputnum):
	#keeps flipping until all happy pancakes or not possible
	x = 1
	#this scope allows for continuous replacement
	result = inputstring
	target = "+" * len(inputstring)
	#easiest way of handling all happy input
	if result == target:
			return 0
	#basically if you have to flip more than you have pancakes its impossible
	while x < len(inputstring)+1:
		result = doAPass(result, inputnum)
		if result == target:
			return x
		x+=1
	return -1


def main():
	while True:
		try:
			inputSize = int(sys.stdin.readline())
			break
		except ValueError:
			print("Input is not an integer. Input again")
	for x in range(1, inputSize+1):
		while True:
			try:
				#get line
				line = sys.stdin.readline()
				#split line
				splitline = [y for y in line.split()]
				#splitline shouild have two elements, first is a string and second is a number
				inputstring = splitline[0]
				inputnum = int(splitline[1])
				#call method to see flip possibilities with these
				resultnum = flip(inputstring, inputnum)
				if resultnum != -1:
					print("Case #"+str(x)+": " + str(resultnum))
				else:
					print("Case #"+str(x)+": IMPOSSIBLE")
				#if made it this far you can break
				break
			except (RuntimeError, TypeError, NameError):
				print("Error processing input for this case! Make sure it looks like \"string\" \"int\"")

if __name__ == "__main__":
    main()