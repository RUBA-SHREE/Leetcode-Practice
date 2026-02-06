from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1:
            return 1
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]>target:
                j-=1
                continue
            if nums[i]+nums[j]<target:
                i+=1
                continue
            else:
                return [i+1,j+1]
