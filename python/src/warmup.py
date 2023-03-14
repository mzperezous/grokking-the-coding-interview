from typing import List

def contains_duplicates(nums: List[int]) -> bool:
    """ Checks for duplicate integers in a list.
        Time complexity: O(n)
        Space complexity: O(n)
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

def is_panagram(sentence: str) -> bool:
    """ Checks if all letters are present in a sentence. Ignores other characters.
        Time complexity: O(n)
        Space complexity: O(n)

        Post-submission notes: Set implementation is cleaner -> O(1) space
            as a HashSet can store 26 chars (at most)
    """
    checker = { char: False for char in "abcdefghijklmnopqrstuvwxyz" }

    for char in sentence:
        if char.isalpha():
            c = char.lower()

            # Default case handles other characters
            if not checker.get(c):
                checker[c] = True

    return not (False in checker.values())

def square_root(x: int) -> int:
    """ Returns the floor of the square root of a non-negative integer.
        Uses binary search, so:
            Runtime complexity: O(log(n))
            Space complexity: O(1)
    """

    # Easy edge cases
    if x < 2:
        return x
    
    left, right = 2, x // 2
    while left <= right:
        
        pivot = left + (right - left) // 2
        guess = pivot * pivot

        if guess > x:
            right = pivot - 1
        elif guess < x:
            left = pivot + 1
        else:
            return pivot
        
    return right