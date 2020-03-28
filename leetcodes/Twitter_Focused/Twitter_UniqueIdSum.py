
"""
945. Minimum Increment to Make Array Unique

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

"""


def UniqueIdSum(nums):
    nums.sort()
    
    cnt = 0 
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i+1]:
            diff = nums[i] - nums[i+1]
            cnt += diff + 1
            nums[i+1] += diff + 1

    return cnt


# nums = [3,2,1,2,1,7]
nums = [1,2,2]
# nums = [1,1,2,2,3,7]

print(UniqueIdSum(nums))




