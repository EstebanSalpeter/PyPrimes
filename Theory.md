# PyPrimes - Theory
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

If we reduce to the subset of odd numbers, it's trivial that any non-prime odd 
number must be factorized in odd numbers as well (as product will produce an 
even whenever at least one factor is even):
q=a*b
This is the generator for every non prime odd number q.

We want to produce the range q(min)<=q<=q(max) with all possible combinations
of a and b's without ommiting any value in range.
We've got a starting point at a=3, to avoid ommissions, increasing its value
by steps of 2.
We'll do the same for the b's, starting from q(max/3) and decreasing until:
b=3 or b=a (it's an ordered pair, b>=a) or q results out of range.

So we obtain the subset of non prime odd numbers, and we must check for the
gaps in one of two ways:
Strategy 0: looping and checking difference between consecutive elements.
Strategy 1: creating another set with all odd numbers in range, and then
obtaining the difference using that method of the set object (this is why we
love Python!).
