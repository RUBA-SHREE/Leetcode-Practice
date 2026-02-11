from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        frstele=float('inf')
        secele=float('inf')
        for num in nums:
            if num<=frstele:
                frstele=num
            elif num<=secele:
                secele=num
            else:
                return True
        return False
#Time:O(n)
#space:o(1)
#Leetcode:334
        