"""
Career Fair :

Given time of arrival for different comapnies, and duration list of companies to a career fair, 
output how many companies would get a chance to perform

looks like finding max No of segments in a list of segments 

solution : https://stackoverflow.com/questions/20929697/how-to-find-maximum-number-of-segments-of-a-infinite-rod-with-given-n-cuts


"""


def maxEvents(arrival, duration):
    n = len(arrival)

    if n <= 1: return n

    duration = [arrival[i] + duration[i] for i in range(n)]

    event_duration = []
    for i in range(n):
        event_duration.append((arrival[i], duration[i]))
    

    event_duration.sort(key= lambda x: x[1])
    print(event_duration)
    # [(1, 3), (4, 5), (3, 6), (5, 7), (7, 8)]
    #    i        i               j

    cnt = 1
    i = 0
    j = 1
    while j < n:
        if event_duration[i][1] <= event_duration[j][0]:
            cnt += 1
            i += 1

        j+= 1

    return cnt



arrival = [1,3,4,5,7]
duration = [2,3,1,2,1]
# must output 4

# arrival = [1, 3, 5, 7, 9, 10, 11]
# duration = [3, 3, 3, 3, 3, 1, 1]
# [(1, 4), (3, 6), (5, 8), (7, 10), (10, 11), (9, 12), (11, 12)]

# summ = [5, 9, 13, 17, 21, 21, 23]


print(maxEvents(arrival, duration))