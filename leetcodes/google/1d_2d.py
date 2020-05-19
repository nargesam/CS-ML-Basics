
def twoD(l, m, n):
    # if m*n < len(l):
    
    two_d_array = [[0]*n for _ in range(m) ]
    # two_d_array = []
    k = 0
    for i in range(len(two_d_array)):
        for j in range(len(two_d_array[0])):
            if k < len(l):
                two_d_array[i][j] = l[k]
            k += 1
    
    

    # for i in range(0,len(l), n):
    #     row = []
    #     for j in range(i, i+m + 1):
    #         row.append(l[j])
    #     two_d_array.append(row)
    return two_d_array

        
    

a = [1,2,3,   4,5,6,7]

# [[1,2,3],[4,5,6]]

m  = twoD(a, 3,3)


def median(l):
    l.sort()
    if len(l)%2 == 1: 
        return l[len(l)//2]

    return (l[len(l)//2 + 1] + l[len(l)//2])//2

for row in m: 
    print(median(row))




