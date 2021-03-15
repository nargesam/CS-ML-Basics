"""
replace all spaces in str with '%20'
"""

def replace(strs):
    return ''.join(['%20' if char==' ' else char for char in strs])


print(replace('   s'))