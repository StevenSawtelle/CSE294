#!/usr/bin/env python3

import sys

#file: maxprofit.py
#Steven Sawtelle

#program goes through a list of given inputs starting with an expected max profit
#it returns the max profit that can be made using the given inputs
#and whether or not that matches the expected max profit. runs in O() time

def process(prices):
    #default vals to be tracked
    minSoFar=prices[0]
    currentMax = prices[0]
    maxProfit =0
    #iterate through each element
    for x in prices:
        #if this element is the min, make it so in the code!
        if x<minSoFar:
            minSoFar = x
        #otherwise see if selling now is the best band for ya buck
        else:
            temp = x-minSoFar
            #if it is, make it so in the code!
            if temp > maxProfit:
                maxProfit = temp
                currentMax = x
    #return them all. round maxProfit cuz python likes to make it ugly
    return (round(maxProfit, 2), minSoFar, currentMax)

def main():
    count=1
    #read all lines from stdin
    for line in sys.stdin:
        #get current line as array of floats
        prices = [float(x) for x in line.split()]
        #no accepted way to handle lists of 1 or less, so just ignore them
        #janky, but works for the given problem
        if len(prices)>1:
            #get values by splitting the first element from a list
            expectedCost = prices[0]
            prices = prices[1:]
            #gets back relevant values for printing nicely
            (actualCost, actualMin, actualMax) = process(prices)
            #write out corresponding pass or fail message
            if actualCost==expectedCost:
                sys.stdout.write("Running test case "+str(count) + "\n"
                                 + "Expected: Max profit is " + str(expectedCost) +"\n"
                                 + "Actual: Buy at "+ str(actualMin)
                                 +", Sell at "+ str(actualMax)
                                 +", Max profit is "+ str(actualCost) +"\n"
                                 +"Test case passed\n");
            else:
                sys.stdout.write("Running test case " + str(count) + "\n"
                                 + "Expected: Max profit is " + str(expectedCost) + "\n"
                                 + "Actual: Buy at " + str(actualMin)
                                 + ", Sell at " + str(actualMax)
                                 + ", Max profit is " + str(actualCost) + "\n"
                                 + "Test case FAILED\n");
        #increment count
        count+=1


#ever-present little driver
if __name__ == "__main__":
    main()