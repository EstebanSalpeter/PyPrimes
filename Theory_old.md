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
This is the generator for every non prime odd number (2n+1).
Simplifying:
n=2ab+a+b
n=b(2a+1)+a

As you can see, we can define:
n: lower half boundary of a non-prime odd.

We can take now our ordered pair (a,b) and two operations: the internal 
product and the internal addition: a times b, a plus b.

If we vary the values a and b, keeping a+b=constant, as the difference b-a
grows, n decreases. We can establish the n(max) and the n(min) values as
n(max)=> a=b, n=2b^2+2b
n(min)=> a=1, n=3b+1

We can see that the curve in the cartesian representation would show a
behaviour that goes from linear to cuadratic.

In order to stay within the field of the theory above, we must ensure to 
generate every non prime odd, otherwise we'll have "gaps" in the resulting
range which belong to the values we've ommited.

We want to produce the range n(min)<=n<=n(max).
If we shall be exhaustive, then we must vary our a and b values from the
combinations of n(min) to n(max), without ommiting any value in range.
We've got a starting point in a=1, so 1<=a<=b (as a=b gives us the maximum 
value our formula is capable of producing).
Now the question is the b. 
When a=1, we've got that n=3b+1, so to obtain the n(max) value b should take
the form b=(n(max)-1)/3.
When a=b, to obtain again n(max), b would be calculated as the roots of the
polynom, b=(-2+-(sqrt(2^2-4*2*n(max)))/2*2
simplifying
b=(-2+-(sqrt(4-8*n(max)))/4
