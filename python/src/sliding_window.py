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