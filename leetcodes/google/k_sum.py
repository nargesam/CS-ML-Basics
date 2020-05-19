"""
Q) Given a sequence of boxes, each with some pens in it and a number X( > 0), 

1 - Find size of smallest interval possible where sum of interval = X

2 - choose two non-overlapping intervals of boxes such that:
        For each interval, the total number of pens in it is exactly X.
        The total number of boxes chosen is as small as possible.
"""


# Q number 1
def sum_k(boxes, x):
    if len(boxes) == 0:
        return 0
    
    dp = [float('inf')]*len(boxes)

    for i in range(len(boxes) -1 , -1, -1):
        sum_i = 0
        j = i
        while j >= 0 and  boxes[j] < x and sum_i<= x:
            sum_i += boxes[j]
            j -=1
        if sum_i == x: 
            dp[i] = i-j - 1
    
    return min(dp)


#Q number 2
def two_k_sum(boxes,x):
    if len(boxes) == 0:
        return 0
    
    dp = [float('inf')]*len(boxes)

    for i in range(len(boxes) -1 , -1, -1):
        sum_i = 0
        j = i
        while j >= 0 and  boxes[j] < x and sum_i<= x:
            sum_i += boxes[j]
            j -=1
        if sum_i == x: 
            dp[i] = i-j - 1

    dp.sort()

    return dp[:2]
    



boxes = [10,2,3,4,5,1,2,2]
x = 5

assert sum_k(boxes, x) == 1
assert two_k_sum(boxes,x) == [1,2]
