from typing import List

def contains_duplicates(nums: List[int]) -> bool:
    """ Checks for """
    seen = {}
    for num in nums:
        if seen.get(num, None) is not None:
            return True
        seen[num] = True
        return False
