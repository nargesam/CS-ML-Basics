"""
Given a string: return how many  palindrome substrings there are in that strings
"""


def palindromeSubCnt(s):

    cnt = 0
    N = len(s)
    p = []
    
    for center in range(2*N - 1):
        left = center//2
        right = left + center%2
        while left >= 0 and  right < N and s[left] == s[right]:
            if left == right:
                p.append(s[left])
            else:
                p.append(s[left:right+1])
            left -=1
            right += 1


    return len(set(p)) 






s = 'abbadaa'
print(palindromeSubCnt(s))
# bb, abba, ada, aa , a, b, d --> 7