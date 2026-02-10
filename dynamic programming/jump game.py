from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*n
        dp[0]=True
        for i in range(n):
            if dp[i]:
                for j in range(1,nums[i]+1):
                    if i+j<n:
                        dp[i+j]=True
        return dp[-1]

#Not optimal
#just a practice of dynamic programming
#Leetcode 55 Jump Game