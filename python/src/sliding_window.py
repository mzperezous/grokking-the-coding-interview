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

    def has_subarray_with_gte_sum(size: int) -> bool:
        window_sum, window_start = 0, 0
        for window_end, num in enumerate(nums):
            window_sum += num

            if window_end >= size:
                if window_sum > s:
                    return True
                window_sum -= nums[window_start]
                window_start += 1

        return False

    for i in range(1, len(nums)):
        if has_subarray_with_gte_sum(i):
            return i

    return 0