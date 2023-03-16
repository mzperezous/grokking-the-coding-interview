from typing import List

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
