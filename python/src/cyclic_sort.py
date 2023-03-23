from typing import List

def cyclic_sort(nums: List[int]) -> List[int]:
    
    i = 0
    n = len(nums) - 1

    while i < len(nums):
        num = nums[i]
        if num == i + 1 or num > n:
            i += 1
        else:
            nums[i], nums[num - 1] = nums[num - 1], nums[i]

    return nums
