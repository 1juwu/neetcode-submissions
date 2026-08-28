"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals:
            return True
        
        # 1. 關鍵修正 1：主動指定用 Interval 的 start 屬性來進行排序
        intervals.sort(key=lambda x: x.start)
        
        # 2. 依序比較前後兩個會議
        for i in range(len(intervals) - 1):
            current_meeting = intervals[i]
            next_meeting = intervals[i + 1]
            
            # 3.用 .end 和 .start 物件屬性拿取時間進行比較
            if current_meeting.end > next_meeting.start:
                return False 
                
        return True