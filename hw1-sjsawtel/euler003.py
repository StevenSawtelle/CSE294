"""
euler003.py
This program finds the prime factors of numbers
    and returns these in a file
Steven Sawtelle
sjsawtel@asu.edu
"""
import math

def isPrime(n):
    #checks if n is prime
    #easy way to handle 1 and 2, not ideal but it works
    if(n==1 or n==2):
        return True
    #if a number is divisible by input then input is not prime
    for x in range(2, int(math.sqrt(n))+1):
        if(n%x==0):
            return False
    #if it can make it the whole way it is prime!
    return True

def makeNiceList(primeFactors):
    #takes list of prime factors to list of lists, with
    #each element being a list of one prime factor and
    #its frequency(exponent)

    #doneList holds prime factors that have been checked
    doneList = []
    #list of lists that will be returned
    factorFrequencyList = []
    #for each prime factor
    for x in primeFactors:
        #if handled, ignore
        if x in doneList:
            pass
        else:
            #if not handled, find how many instances
            count = 1
            for y in primeFactors:
                if(x==y):
                    count+=1
            #add to list of lists
            tempList = [x, count-1]
            factorFrequencyList.append(tempList)
            #mark as handled
            doneList.append(x)
    return factorFrequencyList

def printPrimeFactors(input, factorFrequencyList):
    #outputs prime factors to file as per assignment instructions
    f = open('euler003-test.out', 'a')
    f.write(str(input) + " = ")
    for l in factorFrequencyList:
        f.write("("+str(l[0]))
        #easy way to handle exponents of 1
        if(l[1]!=1):
            f.write("^"+str(l[1])+")")
        else:
            f.write(")")
    f.write('\n')
    f.close()

def generateFactors(n):
    #generates list of factors for number n
    factors = []
    count=0
    #for all numbers <n
    for x in range(1, n):
        #if a number is divisor of n, it is a factor
        #we only need two factors for this algorithm
        #the third factor will be the number we multiply second
            #by to get n
        #with these two we have all we need for prime factorization
        if(n%x==0):
            if(count<2):
                factors.append(x)
                count+=1
            else:
                #multiplicative complement of second factor (i.e. 2*10=20,the 10)
                factors.append(int(n/factors[1]))
                break
    return factors

def process(n):
    #n is number to get primeFactors of
    primeFactors = []
    #get 3 most important factors of a number
    factors = generateFactors(n)
    #identify the important factors
    actOnFactorList = [factors[1], factors[len(factors)-1]]
    #first one will always be prime
    primeFactors.append(actOnFactorList[0])
    #if second one is prime, add it and be done
    if isPrime(actOnFactorList[1]):
        primeFactors.append(actOnFactorList[1])
    #if it's not, recursively call this function using that number
        #as n and add that to the list. this will get all prime factors
        #of a given n
    else:
        tempList = process(actOnFactorList[1])
        for element in tempList:
            primeFactors.append(element)
    return primeFactors

"""
MAIN
"""
#clear file
f = open('euler003-test.out', 'w')
f.write('')
f.close()
#blank list of input values
content=[]
#read from file
with open('euler003-test.in') as f:
    content = f.readlines()
#take away all new lines
content = [x.strip('\n') for x in content]

#for each number in the input file
for input in content:
    input = int(input)
    #if its prime skip all the fancy stuff
    if isPrime(input):
        l = [[input,1]]
        printPrimeFactors(input, l)
    #otherwise generate prime factors
    else:
        #get prime factors
        primeFactors = process(input)
        #get frequency of prime factors
        factorFrequencyList = makeNiceList(primeFactors)
        #output this to file
        printPrimeFactors(input, factorFrequencyList)