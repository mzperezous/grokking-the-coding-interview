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

        Post-submission notes: Set implementation is cleaner
    """
    checker = { char: False for char in "abcdefghijklmnopqrstuvwxyz" }

    for char in sentence:
        if char.isalpha():
            c = char.lower()

            # Default case handles other characters
            if not checker.get(c):
                checker[c] = True

    return not (False in checker.values())
