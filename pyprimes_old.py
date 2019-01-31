#deprecated after algorithm simplification

#author: Esteban Salpeter
#author's email: esteban.salpeter@yahoo.com.ar
def primes_between(min,max,strategy=0):
#init
    #see Theory.md for reference and terminology
    #strategy: 0=looping and finding, other number=set.difference (consumes more memory, expected to be faster)
    #parameters check
    if min>max:
        print ('Error: min parameter must be lower than the max one')
        return 0
    if min%10 in [2,4,6,8,0]:
        min+=1
    if max%10 in [2,4,6,8,0]:
        max-=1
    #the use of a set prevents duplicates
    nonprimeodds=set()
    
    #definitions
    #n: half-lower-bound of a non-prime odd number
    #q: a non-prime odd number
    #a, b: ordered pair (a<=b) used in my algorithm, derived from the assumption of the form (2*n+1) for any odd non-prime number
    
    if strategy==0:
        max+=2
        min-=2

    #let's make only the necessary range by factorization
    a=1
    #let's start filling and factorizing!
    while a<=int((max-3)/6):
        b=int((max-2*a-1)/(4*a+2))
        while b>=int((min-2*a-1)/(4*a+2)):
            #my super formula! 
            q=4*a*b+2*a+2*b+1
            #print(a,b,q)
            if q<min or q>max:
                break
            if q<=max:
                nonprimeodds.add(q)
            b-=1
        a+=1

    #uncomment line below for testing purposes
    print(sorted(nonprimeodds))
        
    if strategy==0:
    #strategy
    #we'll check for the gaps in the nonprimeodds range
    #there could be gaps of 4 or 6 between consecutive odds, meaning there is one or there are two primes there
        primes=set()
        nonprimeodds=sorted(nonprimeodds)
        #uncomment for testing
        print(nonprimeodds)
        #loop from the first up to one before the last (base 0)
        for i in range(0,len(nonprimeodds)-2):
            gap= nonprimeodds[i+1]-nonprimeodds[i]
            for y in range(1,int(gap/2)):
                primes.add(nonprimeodds[i]+2*y)
        
    else:
    #strategy
    #we'll produce all odd numbers in range
    #then we'll produce all non-prime odd numbers in range
    #finally, we'll obtain all prime numbers by difference of both sets
        alloddsinrange=set(range(min,max+1,2))
    
        #uncomment line below for testing purposes
        #print(alloddsinrange)
        #let's use the best of Python collections!
        #use this line if you want to stay using sets instead of lists
        primes=alloddsinrange.difference(nonprimeodds)
        #primes=sorted(alloddsinrange.difference(nonprimeodds))

    #uncomment for testing
    return sorted(primes)
    #return primes

def is_prime(num):
    last = num%10
    if num in [1,2,3,5,7]:
        return True
    if last in [2,4,5,6,8,0]:
        return False
    p=primes_between(num-1,num+1,1)
    if num in p:
        return True
    return False
