#!/usr/bin/env python3

#program to take values from 1/a to 1/b and find the longest repeating decimal
#   sequence in between where a and b are non negative integer inputs. taken
#   from project euler problem 26

import sys

def getRepeat(x):
    #setup
    lis=[]
    stri="0."
    base=10
    count=0
    #if a number is evenly divisible or not
    repeating=True
    #main loop
    while(True):
        #if a base repeats you know its a repeating number
        if (base not in lis):
            lis.append(base)
        else:
            #base=0 means not a repeating decimal!
            if(base==0):
                repeating=False
            break
        #manually go through long division to get important info for each number
        temp=x
        count=0
        while(temp<=base):
            count+=1
            temp+=x
        #add each element of the decimal as its calculated
        stri+=str(count)
        #recalculate base (last step of long division when done manually)
        base= (base-(x*count))*10
    #now use count for where to insert parentheses
    count=0
    while(count<len(lis)):
        if(lis[count]==base):
            break
        count+=1
    #insert parentheses if needed
    if(repeating):
        stri = stri[:count+2]+"("+stri[count+2:]
        stri += ")"
    else:
        stri = stri[:len(stri)-1]
    return stri

def process(x, y, count):
    #each row
    stri = "Test Case "+str(count)+": a = "+str(x)+", b = "+str(y)+"\n"
    longestnum = x
    longestlength=0
    while(x<=y):
        #get correct numbers and track longest as it comes in
        tempstr = getRepeat(x)
        length = len(tempstr)
        if(length>longestlength):
            longestnum=x
            longestlength=length
        stri += "\t1/" + str(x) +" = "+tempstr+"\n"
        x+=1
    #longest length calcs
    stri += "\tLongest recurring cycle: 1/"+str(longestnum)+", "+str(longestlength-4)+" digit(s)\n"
    return stri

def main():
    # get input
    inputs = sys.stdin.readlines()
    content = []
    for line in inputs:
        content.append([int(x) for x in line.split() if x.isdigit()])
    currentNum1 = content[0][0]
    currentNum2 = content[0][1]
    if (currentNum1 == 0):
        return
    i = 1
    while True:
        #write each line of processing to the output file
        if (currentNum1 == 0 or currentNum2 == 0):
            break
        temp = process(currentNum1, currentNum2, i)
        sys.stdout.write(temp)
        currentNum1 = content[i][0]
        currentNum2 = content[i][1]
        i += 1
    return

if __name__ == "__main__":
    main()