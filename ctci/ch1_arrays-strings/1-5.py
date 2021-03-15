"""
compress an string :

aaabbbbaa --> 3a4b2a 

if the len is not compressed, return original str

"""
import collections

def compressed(strs):
    # i=0  j=i+1, while j+1==i, add to tmp, count tmp, add count/char to ret, i = j+1
    i=0
    tmp = ''

    while i <= len(strs)-1:

        j = i+1
        count = 1
        if i == len(strs):
            tmp += '1'
            tmp += strs[i]

        while j<len(strs) and strs[i]==strs[j]:
            count += 1
            j += 1
        tmp += str(count)
        tmp += strs[i]
        i = j

    return tmp if len(tmp)< len(strs) else strs

print(compressed('aaabbbbbba'))


