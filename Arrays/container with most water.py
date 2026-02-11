from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        left,right=0,len(height)-1
        while left<right:
            h=min(height[left],height[right])
            b=right-left
            area=h*b
            res=max(res,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res

#Time:O(n)
#space:O(1)
#Leetcode:11