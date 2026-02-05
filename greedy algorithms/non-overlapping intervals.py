from typing import List

class Solution:
    def eraseOverlapIntervals(self, interval: List[List[int]]) -> int:
        if not interval:
            return 0
        
        interval.sort(key=lambda x:x[1])
        c=1
        last_end=interval[0][1]

        for i in range(1,len(interval)):
            if interval[i][0]>=last_end:
                c+=1
                last_end=interval[i][1]
        return len(interval)-c