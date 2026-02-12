from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        maxfreq=max(c.values())
        c=list(c.values()).count(maxfreq)

        res=(maxfreq-1)*(n+1)+c
        return max(len(tasks),res)