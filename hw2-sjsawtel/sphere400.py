#!/usr/bin/env python3
import sys

def decrypt(columns, encStr):
    #sep1 is first number to increment char counter by
    sep1 = columns*2-1
    #keep track of this value for testing later
    originalSep1 = columns*2-1
    #sep2 is other number to increment char counter by
    #sep1 and sep2 alternate taking control
    sep2 = 1
    #done controls whole word check
    done = False
    #finalString will be costantly filling in with decoded string
    finalString = ""
    #x holds currentCharIndex on each pass
    x=0
    #length of word
    length = len(encStr)
    for y in range(0,columns):
        #y steps through each character
        #reset x to current char
        x=y
        #count tells what number of loop were on
        count=0
        #step through x as appropriate
        while(x<length):
            #first time just add current char (y)
            if(count==0):
                finalString+=encStr[x]
            #add char at oldCharIndex + w/e sep1 is now
            x+=sep1
            #but dont add if x is too big after adding sep1
            if(x<length):
                finalString += encStr[x]
            #add char at oldCharIndex + w/e sep2 is now
            x += sep2
            # but dont add if x is too big after adding sep2
            if (x < length):
                finalString += encStr[x]
            #dont execute the first if on anything but the first pass
            count+=1
        #update sep1 and sep2
        sep1-=2
        sep2+=2
    return finalString

def main():
    # blank list of input values
    content = sys.stdin.readlines()
    # for each pair in the input file
    z=0
    while(z<len(content)):
        #get number, if it is 0 quit
        number = int(content[z])
        if(number==0):
            break
        #get string and calculate decoded value
        decodedString = decrypt(number, content[z+1])
        #write to file
        sys.stdout.write(decodedString)
        z+=2

if __name__ == "__main__":
    main()