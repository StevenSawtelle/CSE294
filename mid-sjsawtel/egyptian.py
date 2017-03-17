#!/usr/bin/env python3

from fractions import Fraction
#easiest way to avoid issues with floating imprecision is use fractions
import sys

def getUnitFraction(num, den, count, unitFractionList):
    #fraction to be used for this iteration of count
    tempFrac = Fraction(1, count)
    while(True):
        tempFrac = Fraction(1, count)
        x=0
        totalminus=0
        #get total value of previous unit fractions
        while(x<len(unitFractionList)):
            if(unitFractionList[x]==0):
                break
            temp2 = Fraction(1, unitFractionList[x])
            totalminus+=temp2
            x+=1
        #when a proper unit factor is found
        if(Fraction(num, den)-totalminus-tempFrac>= 0):
            return count
        #handles too large of denominators
        if(count > 1000000):
            return 0
        count+=1

def process(num, den):
    #default variables
    count = 2
    fraction = Fraction(num, den)
    stri = "" + str(num) + "/" + str(den) + " ="
    done = False
    counter=0
    unitFractionList = []
    #main loop
    while(not done):
        tempFraction = getUnitFraction(num, den, count, unitFractionList)
        #handle case when denominator gets too large
        if(tempFraction == 0):
            count = unitFractionList[len(unitFractionList)-1]
            length = len(str(count))
            stri = stri[:len(stri)-(length+5)]
            del unitFractionList[len(unitFractionList)-1]
        else:
            #add value to list and update strings as needed
            unitFractionList.append(tempFraction)
            if(counter!=0):
                stri += " + 1/"
            else:
                stri += " 1/"
                counter+=1
            stri += str(tempFraction)
            totalminus=0
            total = Fraction(num,den)
            for element in unitFractionList:
                temp = Fraction(1,element)
                totalminus+=temp
                if((total-totalminus)==0):
                    done=True
        count+=1
    stri += "\n"
    return stri

def main():
    #get input
    inputs = sys.stdin.readlines()
    content = []
    for line in inputs:
        content.append([int(x) for x in line.split() if x.isdigit()])
    currentNum1 = content[0][0]
    currentNum2 = content[0][1]
    i=1
    #blank set
    if(currentNum1==0):
        return
    #for each set of numbers a, b get the UFs that total to be a/b
    while True:
        if(currentNum1==0 or currentNum2==0):
            break
        temp = process(currentNum1, currentNum2)
        #print out string
        sys.stdout.write(temp)
        currentNum1 = content[i][0]
        currentNum2 = content[i][1]
        i+=1

if __name__ == "__main__":
    main()