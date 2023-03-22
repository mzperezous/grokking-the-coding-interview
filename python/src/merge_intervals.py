from typing import List

"""    Provided data structures    """

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

"""                                """

def merge(intervals: List[Interval]) -> List[Interval]:
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)
    merged = []
    start, end = intervals[0].start, intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return merged
