class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        ratio=[]
        for i in range(len(val)):
            rat=val[i]/wt[i]
            ratio.append((rat,val[i],wt[i]))
        ratio.sort(reverse=True)
            
        total=0.0
        for rat,val,wt in ratio:
            if capacity==0:
                break
            if wt<=capacity:
                capacity-=wt
                total+=val
            else:
                total+=rat*capacity
                capacity=0
        return round(total,6)
            
            