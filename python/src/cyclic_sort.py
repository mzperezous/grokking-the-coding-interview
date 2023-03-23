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

def find_all_missing_numbers(nums: List[int]) -> List[int]:
    
    i = 0
    missing = []

    while i < len(nums):
        val = nums[i]
        if val != i + 1 and nums[i] != nums[val - 1]:
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
        else:
            i += 1

    for i, val in enumerate(nums):
        if val != i + 1:
            missing.append(i + 1)
        
    return missing

def find_duplicate(nums: List[int]) -> int:
    """ Review: Can return in the original loop with the val != nums[val - 1] check """
    
    i = 0

    while i < len(nums):
        val = nums[i]

        if val != i + 1 and val != nums[val - 1]:
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
        else:
            i += 1

    for i, val in enumerate(nums):
        if i + 1 != val:
            return val
    
def find_all_duplicates(nums: List[int]) -> List[int]:
    
    i, dups = 0, []

    while i < len(nums):
        val = nums[i]

        if val == i + 1:
            i += 1
        elif val == nums[val - 1]:
            dups.append(val)
            i += 1
        else:
            nums[i], nums[val - 1] = nums[val - 1], nums[i]

    return dups

def find_corrupt_pair(nums: List[int]) -> List[int]:
    
    i, n = 0, len(nums)

    corrupt_pair = [-1, -1]  # [duplicate, missing]

    while i < n:
        val = nums[i]
        val_idx = nums[i] - 1

        if val == i + 1:
            i += 1
        else:
            # Duplicate found
            if nums[val_idx] == val:
                corrupt_pair[0] = val
                i += 1
            else:
                nums[i], nums[val_idx] = nums[val_idx], nums[i]

    for i, val in enumerate(nums):
        if val != i + 1 and corrupt_pair[0] != i + 1:
            corrupt_pair[1] = i + 1
            break
        
    return corrupt_pair

def find_smallest_missing_positive_num(nums: List[int]) -> int:

    i, min_missing = 0, 1

    while i < len(nums):
        val = nums[i]

        if val > 0 and val < len(nums) and val != i + 1:
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
        else:
            i += 1

    for i, val in enumerate(nums):
        if val == min_missing:
            min_missing += 1

    return min_missing