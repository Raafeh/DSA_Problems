# Problem Title: Single Number II
"""
Problem Statement: Given an integer array nums where every element appears 
three times except for one, which appears exactly once. Find the single element and return it.
Example:
Input: nums = [2,2,3,2]
Output: 3
"""
class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
    
# Time Complexity: O(n)
# Space Complexity: O(1)

# Testing the solution
s = Solution()
print(s.singleNumber([2,2,3,2]))  # Output: 3
