from typing import List

def max_sum_subarray(size: int, nums: List[int]) -> int:

    max_sum = None
    
    window_sum, window_start = 0, 0
    for window_end, num in enumerate(nums):
        window_sum += num

        if window_end >= size - 1:
            if max_sum is None:
                max_sum = window_sum
            max_sum = max(window_sum, max_sum)
            window_sum -= nums[window_start]
            window_start += 1

    return max_sum

def smallest_subarray_with_gte_sum(s: int, nums: List[int]) -> int:
    """ Review this one """

    min_len = None
    window_sum, window_start = 0, 0
    for window_end, num in enumerate(nums):
        window_sum += num

        while window_sum >= s:
            if min_len is None:
                min_len = window_end - window_start + 1
            else:
                min_len = min(min_len, window_end - window_start + 1)
            window_sum -= nums[window_start]
            window_start += 1
    if min_len is None:
        return 0
    return min_len

def longest_substring_with_lte_k_distinct(s: str, k: int) -> int:
    max_len = 0

    window_start = 0
    for window_end, char in enumerate(s):
        num_distinct = len(set(s[window_start:window_end+1]))

        if num_distinct > k:
            window_start += 1
        else:
            max_len = max(max_len, window_end + 1 - window_start)

    return max_len