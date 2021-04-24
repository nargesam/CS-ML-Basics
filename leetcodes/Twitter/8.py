# 8- https://leetcode.com/discuss/interview-question/374846/Twitter-or-OA-2019-or-University-Career-Fair



def careerFair(arrival, duration):
    
    assert len(arrival) == len(duration)
    
    end = [arrival[i] + duration[i] for i in range(len(arrival))]

    assert len(end) == len(arrival)

    dur = [(arrival[i], end[i]) for i in range(len(arrival)) ]
    dur.sort(key = lambda x: x[1])

    cnt = 1 
    i = 0
    j = 1
    while j < len(arrival):
        if dur[i][1] <= dur[j][0]:
            cnt += 1
            i += 1
        j += 1
    
    return cnt



arrival = [1,3,4,5,7]
duration = [2,3,1,2,1]

# [(1, 3), (3, 6), (4, 5), (5, 7), (7, 8)]
# must output 4


# arrival = [1, 3, 5, 7, 9, 10, 11]
# duration = [3, 3, 3, 3, 3, 1, 1]
# [(1, 4), (3, 6), (5, 8), (7, 10), (10, 11), (9, 12), (11, 12)]

print(careerFair(arrival, duration))