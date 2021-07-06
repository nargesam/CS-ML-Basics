# 3-https://leetcode.com/discuss/interview-question/406652/Twitter-or-OA-2019-or-Anagram-Difference
import collections
def make_anagram(s, t):
    if len(s)!=len(t):
            return -1
            
    sc = collections.Counter(s)
    tc = collections.Counter(t)        
    
    cnt = 0
    for char in sc: 
        if char not in tc: 
            cnt += sc[char]
        if char in tc and sc[char] > tc[char]  : 
            cnt += sc[char] - tc[char]
    
    return cnt 

print(make_anagram('abc', 'bcd'))