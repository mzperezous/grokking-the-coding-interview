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

def reverse_vowels(s: str) -> str:
    """ Returns a string with the vowels of s in reverse order.
        Time complexity: O(n)
        Space complexity: O(n)

        Post-submission notes: Two pointers pattern also works well here
    """
    VOWELS = "aeiou"
    track_indices: List[int] = []
    characters: List[str] = []

    for i, char in enumerate(s):
        characters.append(char)
        if char.lower() in VOWELS:
            track_indices.append(i)

    if len(track_indices) > 0:
        track_indices = list(reversed(track_indices))
        vowel_index_to_add = 0

        res = [""] * len(s)
        for i in range(len(res)):
            if i in track_indices:
                res[i] = s[track_indices[vowel_index_to_add]]
                vowel_index_to_add += 1
            else:
                res[i] = s[i]
                
        return "".join(res)
    
    else:
        return s

def is_palindrome(s: str) -> bool:
    """ Returns a boolean representing whether s is a palindrome using two pointers.
        Time complexity: O(n)
        Space complexity: O(1)

        Post-submission notes: Investigate how the map, filter, join combo affects space (shouldn't)
    """
    s_chars = ''.join(map(lambda x: x.lower(), filter(lambda x: x.isalpha(), s)))
    
    # Two pointers
    left, right = 0, len(s_chars) - 1

    while right > left:

        if s_chars[left] != s_chars[right]:
            return False
        
        left += 1
        right -= 1

    return True