""""
implement reverse string

"""
def reverse(strs):
    l,r = 0, len(strs)-1
    temp = list(strs)
    while l< r:
        temp[l], temp[r] = temp[r], temp[l]
        l += 1
        r-= 1
    return ''.join(temp)

print(reverse('sa lam '))

