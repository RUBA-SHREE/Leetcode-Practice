class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""
        res=''
        for i in range(len(s)):
            for j in range(i,len(s)):
                strs=s[i:j+1]
                if strs==strs[::-1]:
                    if len(res)<len(strs):
                        res=strs
        return res
#Leetcode 5. Longest Palindromic Substring  