
"""
0- Given a random generator function that returns 0,1 biased probabilty, generate 0,1 wirh uniform prob?

00- 0- Given a random generator function that returns 0,1 with fair probabilty, generate 0,1 wirh biased prob?


1- Given a random generator function that returns 0,1 biased probabilty, generate [0,6] wirh uniform prob?


2 - Given a biased 6-sided die of unknown bias, can we simulate a fair coin toss?

3- 

"""
# 0 = .60
# 1 = .40

from random import randint

def generated():

    r = randint(0,99)
    return 1 if r < 25 else 0

def unbiasedcoin():
    while True: 

        first = generated()
        second = generated()

        if first!=second:
            return first


def biasedcoin():
    
    first = randint(0,1)
    second = randint(0,1)
    # 00, 01, 10 --> 0 , 11 --> 1, 75/25 probability

    while True: 
        if first + second ==2: 
            return 1
        elif first+second == 1: 
            return 0




def fairDie():
    # AAA
    # AAB
    # ABA
    # BAA
    # BAB
    # BBA 
    # ABB
    # BBB 
    while True: 
        first = unbiasedcoin()
        second = unbiasedcoin()
        third = unbiasedcoin()

        if first==0 and second==0 and third==0: 
            return 1
        if first==0 and second==0 and third==1: 
            return 2
        if first==0 and second==1 and third==0: 
            return 3
        if first==1 and second==0 and third==0: 
            return 4
        if first==1 and second==1 and third==0: 
            return 5
        if first==1 and second==0 and third==1: 
            return 6
        if first==0 and second==1 and third==1: 
            return 7







print(unbiasedcoin())
print(fairDie())


# 01
# 10 
# 11 , 00 


# 000 4*4*4
# 001 4*4*6
# 010 4*4*6
# 100 4*4*6
# 011 4*6*6
# 101 4*6*6
# 110 4*6*6
# 111 6*6*6