class Solution:
    def candy(self, ratings: List[int]) -> int:
        s=1
        i=1
        n=len(ratings)
        if n==0:
            return 0
        while i<n:
            if ratings[i]==ratings[i-1]:
                s+=1
                i+=1
                continue
            peak=1
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                s+=peak
                i+=1
            down=1
            while i<n and ratings[i]<ratings[i-1]:
                down+=1
                s+=down-1
                i+=1
            
            if down > peak:
                s+=(down-peak)
        return s
        