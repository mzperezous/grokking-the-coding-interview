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

            if end == interval_1.end:  # interval_1.end < interval_2.end
                i += 1
            else:
                j += 1

    return result

def has_conflicting_appointments(appts: List[Interval]) -> bool:
    
    appts.sort(key=lambda x: x.start)

    for i in range(1, len(appts)):
        if appts[i - 1].end > appts[i].start:
            return True

    return False

""" Challenge Problems """

class Meeting(Interval):
    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end

def minimum_meeting_rooms(meetings: List[Meeting]) -> int:
    """ Review this one """

    from heapq import heappop, heappush
    
    if len(meetings) == 0:
        return 0
    
    rooms = 1
    min_heap = []

    meetings.sort(key=lambda x: x.start)

    for meeting in meetings:
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
        heappush(min_heap, meeting)
        rooms = max(rooms, len(min_heap))

    return rooms

class Job(Interval):
    def __init__(self, start, end, load):
        super().__init__(start, end)
        self.load = load
        
def max_cpu_load(jobs: List[Job]) -> int:
    
    max_load = jobs[0].load
    load_track = 0
    first_overlap = True

    jobs.sort(key=lambda x: x.start)

    for i in range(1, len(jobs)):
        job_1, job_2 = jobs[i - 1], jobs[i]

        # Sum loads of overlapping jobs
        if job_1.end > job_2.start:
            if first_overlap:
                load_track += job_1.load + job_2.load
                first_overlap = False
            else:
                load_track += job_2.load
        else:
            # If no overlaps found, use job_2 as comparison
            max_load = max(max_load, load_track if load_track != 0 else job_2.load)
            load_track = 0
            first_overlap = True

    return max(max_load, load_track)
