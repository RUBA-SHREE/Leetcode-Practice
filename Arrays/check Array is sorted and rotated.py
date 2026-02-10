from typing import List
#Time-O(n)
#space-O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                c+=1
                if c>1:
                    return False
        return True

#Time-O(n^2)
#Space-O(n)
class Solution:
    def check(self, nums: List[int]) -> bool:
        sor=sorted(nums)
        if sor==nums:
            return True
        for i in range(len(nums)):
            c=nums[-i:]+nums[:-i]
            if c==sor:
                return True
        return False