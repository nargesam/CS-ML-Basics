"""
write an algorithms to see if a string has all unique characters. 
what if you didn't have to use additional data structures? 
"""

import unittest 

class ArrayStrings():
    def __init__(self, strs):
        self.strs = strs 
    
    def uniqueNewDS(self):
        return len(set(self.strs))==len(self.strs)

    def unique(self):
        for char in self.strs:
            if self.strs.count(char)!=1:
                return False
        return True

obj = ArrayStrings("ihavenonew")
print(obj.uniqueNewDS())
print(obj.unique())

# class TestArrayStrings(unittest.TestCase):

#     def test_uniqueNewDS(self):
#         self.assertEqual()
