# 1- https://leetcode.com/discuss/interview-question/374440/Twitter-or-OA-2019-or-Weird-Faculty


def weird_faculty(qs):

    qs = [-1  if i==0 else 1 for i in qs]
    print(qs)
    n = len(qs)
    my_friend = sum(qs)
    my_answers =  0

    for i in range(n):
        print(my_answers, my_friend)
        if my_answers > my_friend:
            return i
        my_answers += qs[i]
        my_friend -= qs[i]

    return n 


print(weird_faculty([1,1,1,0 , 1]))

