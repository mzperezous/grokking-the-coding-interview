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

def find_missing_number(nums: List[int]) -> int:

    i, n = 0, len(nums)

    while i < len(nums):
        val = nums[i]

        if i == val or n == val:
            i += 1
        else:
            nums[i], nums[val] = nums[val], nums[i]

    for i, val in enumerate(nums):
        if i != val:
            return i

    return n