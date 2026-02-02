class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=t=tw=0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                if f>=1:
                    f-=1
                    t+=1
                else:
                    return False
            elif i==20:
                if t>=1 and f>=1:
                    t-=1
                    f-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        else:
            return True
            


        