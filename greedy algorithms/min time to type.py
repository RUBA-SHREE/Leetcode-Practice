class Solution:
    def minTimeToType(self, word: str) -> int:
        c=0
        s='a'
        for ch in word:
            clockwise=abs(ord(ch)-ord(s))
            c+=min(clockwise,26-clockwise)
            c+=1
            s=ch
        return c
#Leetcode 1974 Minimum Time to Type Word Using Special Typewriter