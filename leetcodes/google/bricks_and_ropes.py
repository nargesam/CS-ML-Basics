"""
Given a zero-inexed array H of height of buildings, number of bricks b and number of ropes r. You start your journey from buiding 0 and move to adjacent building either using rope or bricks. You have limited number of bricks and ropes.
While moving from ith building to (i+1)th building,

if next building's height is less than or equal to the current buiding's height, you do not need rope or bricks.
if next building's height is greater than current buiding's height, you can either use one rope or (h[i+1] - h[i]) bricks.
So, question is How far can you reach from 0th buiding if you use bricks and ropes optimally? return index of building till which you can move.


input : H = [4,2,7,6,9,11,14,12,8], b = 5, r = 2
Output: 8
Explanation: use rope to move from index 1 to index 2. 
use 3 bricks to move from index 3 to index 4. 
use 2 bricks to move from index 4 to index 5. 
use rope to move from index 5 to index 6. 
so we can reach at the end of the array using 2 ropes and 5 bricks. 



"""


def _can_walk(buildings, ropes, bricks):
    
    steps_needed = []
    for i in range(len(buildings)-1):
        if buildings[i] < buildings[i+1]:
            steps_needed.append(buildings[i+1] - buildings[i])
        else:
            steps_needed.append(0)
        
    steps_needed.sort()
        
    if ropes >0:
        steps_needed = steps_needed[:-ropes]

    return sum(steps_needed) <=  bricks

    # return True

def get_brick_rope_index(buildings, ropes, bricks):
    
    for i in range( len(buildings) + 1):
        if not  _can_walk(buildings[:i], ropes, bricks):
            return i-2
    
    return len(buildings) - 1



H = [4,2,7,6,9,11,14,12,8]
b = 5
r = 2

print(get_brick_rope_index(H, r, b))

