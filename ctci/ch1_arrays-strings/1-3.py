"""
write a method to see given two strings, one is permutation of the other

I used counter method (o(n)), but you can also check if by sorting the strings, 
they become identical (o(nlogn)). 

"""

import collections

def ispermutation(s1, s2):
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)

    return c1==c2

print(ispermutation('ABC', 'ACB'))
print(ispermutation('ABC', 'AB'))
print(ispermutation('ABC', 'ABD'))

