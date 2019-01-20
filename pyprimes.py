#author: Esteban Salpeter
#author's email: esteban.salpeter@yahoo.com.ar
from math import sqrt
def primes_between(min,max,strategy=0):
#init
        #strategy: 0=looping and finding, other number=set.difference (consumes more memory)
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
        #method
        #we'll produce all odd numbers in range
        #then we'll produce all non-prime odd numbers in range
        #finally, we'll obtain all prime numbers by difference of both sets
        
        #definitions
        #n: half-lower-bound of a non-prime odd number
        #m, l: ordered pair (m>=l) used in my algorithm, derived from the assumption of the form (2*n+1) for any odd non-prime number
        #mx: maximum value for m and l to produce max when m=l
        #mn: minimum value of n to produce min (whatever values for m and l)
        
        #let's make only the necessary range by factorization
        #see Theory.md for reference on this range determination
        if strategy==0:
                max+=2
                min-=2
        mx,mn = int((max)/2), int(sqrt(min))
        m=mx

        #let's start filling and factorizing!
        while m>=mn:
                l=1
                while l<=m:
                        #my super formula! generator of every nonprime odd number's half-lower-bound
                        n=m*l*2+m+l
                        if n*2+1>max:
                                break
                        if (n*2+1<=max) & (n*2+1>=min):
                                nonprimeodds.add(n*2+1)
                        l+=1
                m-=1
                
        #uncomment line below for testing purposes
        #print(nonprimeodds)
                
        if strategy==0:
                primes=set()
                nonprimeodds=sorted(nonprimeodds)
                #uncomment for testing
                #print(nonprimeodds)
                for i in range(0,len(nonprimeodds)-2):
                        gap= nonprimeodds[i+1]-nonprimeodds[i]
                        for y in range(1,int(gap/2)):
                                primes.add(nonprimeodds[i]+2*y)
                
        else:
                alloddsinrange=set(range(min,max+1,2))
        
                #uncomment line below for testing purposes
                #print(alloddsinrange)
                #let's use the best of Python collections!
                #use this line if you want to stay using sets instead of lists
                primes=alloddsinrange.difference(nonprimeodds)
                #primes=sorted(alloddsinrange.difference(nonprimeodds))
                
        return sorted(primes)

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
