from typing import Dict, List

def max_sum_subarray(size: int, nums: List[int]) -> int:

    max_sum = None
    
    window_sum, window_start = 0, 0
    for window_end, num in enumerate(nums):
        window_sum += num

        if window_end >= size - 1:
            if max_sum is None:
                max_sum = window_sum
            max_sum = max(window_sum, max_sum)
            window_sum -= nums[window_start]
            window_start += 1

    return max_sum

def smallest_subarray_with_gte_sum(s: int, nums: List[int]) -> int:
    """ Review this one """

    min_len = None
    window_sum, window_start = 0, 0
    for window_end, num in enumerate(nums):
        window_sum += num

        while window_sum >= s:
            if min_len is None:
                min_len = window_end - window_start + 1
            else:
                min_len = min(min_len, window_end - window_start + 1)
            window_sum -= nums[window_start]
            window_start += 1
    if min_len is None:
        return 0
    return min_len

def longest_substring_with_lte_k_distinct(s: str, k: int) -> int:
    max_len, window_start = 0, 0

    for window_end, _ in enumerate(s):
        num_distinct = len(set(s[window_start:window_end+1]))

        if num_distinct > k:
            while len(set(s[window_start:window_end + 1])) > k and window_start <= window_end:
                window_start += 1
        else:
            max_len = max(max_len, window_end + 1 - window_start)

    return max_len

def fruits_into_baskets(fruits: List[str]) -> int:
    
    max_fruits, window_start = 1, 0

    for window_end, _ in enumerate(fruits):
        num_fruits = len(set(fruits[window_start:window_end + 1]))

        if num_fruits <= 2:
            max_fruits = max(max_fruits, window_end + 1 - window_start)
        else:
            while len(set(fruits[window_start:window_end + 1])) > 2:
                window_start += 1

    return max_fruits

def length_of_longest_substring_after_k_substitution(s: str, k: int) -> int:
    import operator

    freq = {}
    w_start, max_len = 0, 0

    for w_end, char in enumerate(s):
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

        main = max(freq.items(), key=operator.itemgetter(1))[0]
        others = sum(freq[char] for char in freq if char != main)

        if others <= k:
            max_len = max(max_len, w_end + 1 - w_start)
        else:
            while others > k and w_end >= w_start:
                freq[s[w_start]] -= 1
                w_start += 1
                main = max(freq.items(), key=operator.itemgetter(1))[0]
                others = sum(freq[char] for char in freq if char != main)

    return max_len

def length_of_longest_1s_after_k_substitutions(binary: List[int], k: int) -> int:

    w_start, num_zeros, max_len = 0, 0, 0

    for w_end, digit in enumerate(binary):
        if digit == 0:
            num_zeros += 1
        
        while num_zeros > k:
            if binary[w_start] == 0:
                num_zeros -= 1
            
            w_start += 1

        max_len = max(max_len, w_end + 1 - w_start)

    return max_len

def permutation_in_string(s: str, pattern: str) -> bool:
    from collections import Counter

    frequency = dict(Counter(pattern.lower()))

    window_start, matched = 0, 0
    for window_end, char in enumerate(s):
        # This character matches our pattern, mark it
        if char in frequency:
            frequency[char] -= 1
            if frequency[char] == 0:
                matched += 1

        # We've found all of the matched characters
        if matched == len(frequency):
            return True
        
        # If we didn't return and our window is big enough, 
        #   slide it and reset our checks on s[window_start]
        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in frequency:
                if frequency[left_char] == 0:
                    matched -= 1
                frequency[left_char] += 1

    return False