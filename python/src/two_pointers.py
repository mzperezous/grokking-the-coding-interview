from typing import Iterable, List

def pair_with_target_sum(nums: List[int], target: int):
    """ Returns indices of elements that add up to target if they exist.
            Else, returns [-1, -1]
        Time complexity: O(n)
        Space complexity: O(1)
    """

    l, r = 0, len(nums) - 1
    while r > l:
        check = nums[l] + nums[r]

        if check == target:
            return [l, r]
        elif check > target:
            r -= 1
        else:
            l += 1

    return [-1, -1]

def remove_duplicates(nums: List[int]) -> int:
    """ Removes the duplicates from nums in place and returns the updated length.
        Time complexity: O(n)
        Space complexity: O(1)
    """
    if len(nums) == 1:
        return 1

    curr, next_non_dup = 0, 1
    while next_non_dup < len(nums):
        # Find all duplicates
        if nums[curr] == nums[next_non_dup]:
            next_non_dup += 1
            continue
        
        # Remove duplicates when differing element found
        else:
            for i in range(curr, next_non_dup - 1):
                nums.pop(i)
            curr += 1
            next_non_dup = curr + 1

    # If last element is repeating, remove dups
    if curr < len(nums) - 1:
        for i in range(curr + 1, next_non_dup):
            nums.pop(i)

    return len(nums)

def square_sorted(nums: List[int]) -> List[int]:
    """ Return an array of the squares of the numbers in nums.
        Time complexity: O(n)
        Space complexity: O(n)
    """
    
    # Simple map if no negatives
    if nums[0] >= 0:
        return [x ** 2 for x in nums]
    
    length = len(nums)
    l, r = 0, length - 1
    squared_nums = [0 for x in range(length)]
    curr_idx = length - 1

    while curr_idx >= 0:
        l_squared, r_squared = nums[l] ** 2, nums[r] ** 2
        if l == r:
            squared_nums[curr_idx] = l_squared
            curr_idx -= 1
        elif l_squared == r_squared:
            squared_nums[curr_idx] = l_squared
            squared_nums[curr_idx - 1] = r_squared
            l += 1
            r -= 1
            curr_idx -= 2
        elif l_squared > r_squared:
            squared_nums[curr_idx] = l_squared
            l += 1
            curr_idx -= 1
        else:
            squared_nums[curr_idx] = r_squared
            r -= 1
            curr_idx -= 1

    return squared_nums
