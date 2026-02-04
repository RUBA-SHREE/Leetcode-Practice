class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        meeting=list(zip(start,end))
        meeting.sort(key=lambda x:x[1])
        c=1
        last_end=meeting[0][1]
        for i in range(1,len(meeting)):
            if meeting[i][0]>last_end:
                c+=1
                last_end=meeting[i][1]
        return c