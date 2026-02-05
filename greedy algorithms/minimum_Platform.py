class Solution:    
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        c=0
        i=j=0
        n=len(arr)
        plat=0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                plat+=1
                c=max(c,plat)
                i+=1
            else:
                plat-=1
                j+=1
        return c
                
        