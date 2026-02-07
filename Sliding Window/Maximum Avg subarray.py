class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        window_max=window_sum

        for i in range(k,len(nums)):
            window_sum+=nums[i]
            window_sum-=nums[i-k]
            window_max=max(window_max,window_sum)
        return window_max/k
#leetcode 643 Maximum Average Subarray I