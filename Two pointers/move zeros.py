class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        while i<len(nums):
            nums[i]=0
            i+=1
        
        
#leetcode 283 Move Zeroes