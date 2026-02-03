class Solution:
    def checkValidString(self, s: str) -> bool:
        open=0
        close=0

        for i in s:
            if i=='(':
                open+=1
                close+=1
            elif i==')':
                open-=1
                close-=1
            else:
                open-=1
                close+=1
            if close<0:
                return False
            else:
                if open<0:
                    open=0
        return open==0
