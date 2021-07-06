"""
write a function to sample from a multinomial distribution, 
		
Given a random generator function that returns 0,1 biased probabilty, generate 0,1 wirh uniform prob?

Given a random generator function that returns 0,1 with fair probabilty, generate 0,1 wirh biased prob?

Given a random generator function that returns 0,1 biased probabilty, generate [0,6] wirh uniform prob?


Given a biased 6-sided die of unknown bias, can we simulate a fair coin toss?

Given a sorted array, apply the transformation ax^2 + bx + c and return new sorted array. Follow up: how do we extend the idea to cubic polynomial?
"""

import random

def sample_multi(p):
    k = len(p)
    p.sort() #o(klogk)

    # calculate cumulative intervals 
    for i in range(1,k): #o(k)
        p[i] += p[i-1]
    
    n = random.random()
    # n = .7
    print(p)
    print(n)

    # search for a and index i  in p where   p[i-1]<n<p[i]
    # o(logn) binary search or o(n) linear scan 

    l,r = 0, k-1
    while l<=r: 
        mid = (l+r)//2

        if mid==0 and n  <= p[mid]:
            return mid 
        elif mid == k-1 and n> p[mid-1]:
            return mid
        elif n <= p[mid] and n> p[mid-1]:
            return mid
        elif p[mid] > n: 
            r = mid-1
        else: 
            l = mid +1 
        

def biased_generator(p):
    n = random.random()
    if n <= p: 
        return 0:
    return 1

def faircoin_from_biased_generator(p):
    biased_coin1 = biased_generator(p)
    biased_coin2 = biased_generator(p)
    while biased_coin1==biased_coin2: 
        biased_coin1 = biased_generator(p)
        biased_coin2 = biased_generator(p)
        # outcome: 00,01,01,11  ==> filter to always get 00 or 11 
    return biased_coin1


def biasedcoin_to_fairdie(p):

    # 000, 001, 010, 100, 101, 110, 011, 111

    while True: 
        coin1 = faircoin_from_biased_generator(p)
        coin2 = faircoin_from_biased_generator(p)
        coin3 = faircoin_from_biased_generator(p)
        
        if coin1==0 and coin2==0 and coin3==1: 
            return 0
        if coin1==0 and coin2==1 and coin3==0: 
            return 1
        if coin1==1 and coin2==0 and coin3==0: 
            return 2
        if coin1==1 and coin2==0 and coin3==1: 
            return 3
        if coin1==1 and coin2==1 and coin3==0: 
            return 4
        if coin1==0 and coin2==1 and coin3==1: 
            return 5
        

def sort_transformation(p):
    pass 


print(sample_multi([0.1, 0.3, 0.4, 0.2]))