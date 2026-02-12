from collections import defaultdict
class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            freq=defaultdict(int)
            mx=0
            dis=0
            for j in range(i,n):
                ch=s[j]
                freq[ch]+=1

                if freq[ch]==1:
                    dis+=1
                mx=max(mx,freq[ch])
                if dis*mx==j-i+1:
                    ans=max(ans,j-i+1)
        return ans

        