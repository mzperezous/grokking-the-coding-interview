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

def insert(intervals: List[Interval], new: Interval) -> List[Interval]:

    merged, i = [], 0

    # Skip over non overlapping intervals and log them
    while i < len(intervals) and new.start > intervals[i].end:
        merged.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < len(intervals) and intervals[i].start <= new.end:
        new.start = min(intervals[i].start, new.start)
        new.end = max(intervals[i].end, new.end)
        i += 1

    merged.append(new)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged

def intersection(l1: List[Interval], l2: List[Interval]) -> List[Interval]:
    result = []

    i, j = 0, 0
    start, end = None, None

    while i < len(l1) and j < len(l2):
        interval_1, interval_2 = l1[i], l2[j]

        # No overlaps
        if interval_1.end < interval_2.start:
            i += 1
            continue
        elif interval_2.end < interval_1.start:
            j += 1
            continue
        # Overlaps
        else:
            start = max(interval_1.start, interval_2.start)
            end = min(interval_1.end, interval_2.end)
            result.append(Interval(start, end))

            if end == interval_1.end:
                i += 1
            else:
                j += 1

    return result