from typing import List
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_=float('inf')
        max_=0
        for i in range(len(nums)):
            if nums[i]<min_:
                min_=nums[i]
            else:
                max_=max(max_,nums[i]-min_)
        return max_
#Leetcode 121 Best Time to Buy and Sell Stock