"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        start_pointer, end_pointer = 0, 0
        curr_count, max_count = 0, 0

        while start_pointer < len(start):
            if start[start_pointer] < end[end_pointer]:
                curr_count += 1
                start_pointer += 1
            else:
                curr_count -= 1
                end_pointer += 1
            
            max_count = max(curr_count, max_count)

        return max_count

        