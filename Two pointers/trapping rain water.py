from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        lm=0
        rm=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=lm:
                    lm=height[left]
                else:
                    water+=lm-height[left]
                left+=1
            else:
                if height[right]>=rm:
                    rm=height[right]
                else:
                    water+=rm-height[right]
                right-=1
        return water
                
#leetcode 42 Trapping Rain Water