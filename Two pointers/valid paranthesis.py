#Leetcode 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=s.lower()
        i=0
        j=len(s)-1
        while i<j:
            if not res[i].isalnum():
                i+=1
                continue
            if not res[j].isalnum():
                j-=1 
                continue
            if res[i]!=res[j]:
                return False
                break
            i+=1
            j-=1
        else:
            return True