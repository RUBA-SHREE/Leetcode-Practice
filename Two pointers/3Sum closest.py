from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float('inf')
        for fix in range(0,len(nums)-2):
            if fix!=0 and nums[fix]==nums[fix-1]:
                continue
            l,r=fix+1,len(nums)-1
            while l<r:
                s=nums[fix]+nums[l]+nums[r]
                if abs(s-target)<abs(ans-target):
                    ans=s
                if s<=target:
                    l+=1
                elif s>target:
                    r-=1
        return ans