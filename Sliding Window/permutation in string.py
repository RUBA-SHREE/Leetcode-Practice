class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        check=len(s1)
        for i in range(len(s2)-check+1):
            
            window=s2[i:i+check]
            if sorted(window)==sorted(s1):
                return True
        else:
            return False
#Leetcode 567 Permutation in String