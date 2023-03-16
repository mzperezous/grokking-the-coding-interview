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