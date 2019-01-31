# PyPrimes - Theory
#deprecated after algorithm simplification

This is part of the package PyPrimes by Esteban Salpeter
autor's email: esteban.salpeter@yahoo.com.ar

This document is intended to support theoretically the algorithms implemented
in the pyprimes.py functions.

The main idea in this approach is that assuming we cannot generate prime
numbers, we actually can generate non primes; more precisely, non prime odds.
Then, analysing the resulting range of non prime odds generated, there should be
"gaps", that is to say, differences between consecutive elements that exceed the
expected of 2 for two consecutive odds. Those "gaps" ARE PRIMES with 100%
accuracy.

The resulting algorithm will not be probably the most efficient, but its
strenght lies in the accuracy: it's 100%, doesn't require the "services" of 
probabilistics. Specially when calculating large prime numbers, the accuracy
remains 100%.

Let's start.

Based on the Fundamental Theorem of Aritmetics, it can be said that:
given the ordered pair (a,b) with both belonging to Naturals, the internal
product of the elements, a times b, may be considered as generator for every
non-prime natural number.

If we reduce to the subset of odd numbers, representable by the formula
(2n+1), it's trivial that any non-prime odd number must be factorized in odd
numbers as well (as product will produce an even whenever at least one factor
is even):
2n+1=(2a+1)(2b+1)
2n+1=4ab+2a+2b+1
This is the generator for every non prime odd number q=(2n+1).
q=4ab+2a+2b+1

Simplifying:
n=2ab+a+b
n=b(2a+1)+a
q=b(4a+2)+2a+1

As you can see, we can define:
n: lower half boundary of a non-prime odd.

We want to produce the range q(min)<=q<=q(max) with all possible combinations
of a and b's without ommiting any value in range.
We've got a starting point in a=1, to avoid ommissions, increasing its value
by steps of 1.
So we resolve b in the formula, replacing the q by q(min) and q(max), what
gives us the range of b's for a=1.
b=(q-2a-1)/(4a+2)
b(min)=(q(min)-2a-1)/(4a+2)
b(max)=(q(max)-2a-1)/(4a+2)

Then we'll loop within the b-range and obtain all q's in range.
Next step would be to continue the major loop, the a-range, step 1 (a=2,a=3,...)
The b-loop will be then be determined before starting (no trial needed).
The a-loop will need to be tested, so when it gives us an out of range q, it
should break (or move forward to enter if the direction of the b-loop goes
from the out of range into the range).
