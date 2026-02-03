class Solution:
    def findMin(self, n):
       rupees=[10,5,2,1]
       c=0
       i=0
       while n>0 and i<len(rupees):
           if n>=rupees[i]:
               c+=1
               n-=rupees[i]
           else:
                i+=1
       return c
               
       