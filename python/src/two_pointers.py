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
            break
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


def triplet_sum_to_zero(nums: List[int]) -> List[List[int]]:
    """ Returns all triplets in nums that sum to zero.
            Uses helper function to sum to inverse of any given element.
        Time complexity: O(n*log(n) + n^2) => O(n^2)
        Space complexity: O(n)
    """
    triplets = []
    sorted_nums = sorted(nums)

    def pair_sum_to_number(target: int, target_idx: int, left_idx: int):
        l, r = left_idx, len(sorted_nums) - 1

        for i, val in enumerate(sorted_nums[left_idx:]):
            # Only look for unique values
            if i > 0 and val == sorted_nums[i - 1]:
                continue
            
            l_val, r_val = sorted_nums[l], sorted_nums[r]

            if l >= r:
                return

            if l_val + r_val + target == 0:
                triplets.append([target, l_val, r_val])
                l += 1
                r -= 1
            elif l_val + r_val + target > 0:
                r -= 1
            else:
                l += 1

        return

    for i, val in enumerate(sorted_nums):
        l = i + 1

        if not len(sorted_nums[l:]) < 3:
            pair_sum_to_number(val, i, l)

    return triplets

def triplet_sum_closest_to_target(nums: List[int], target: int) -> List[int]:
    """ Returns the sum of the triplet with the sum closest to target.
            If two are equidistant, return the smaller sum.
        Time complexity: O(n^2)
        Space complexity: O(n)

        Post-submission notes: Space complexity is O(n) because of sorting
    """
    sorted_nums = sorted(nums)

    triplet = None
    triplet_sum = None

    for i, val in enumerate(sorted_nums):
        l, r = i + 1, len(sorted_nums) - 1

        while r > l:
            l_val, r_val = sorted_nums[l], sorted_nums[r]
            check_sum = l_val + r_val + val

            if triplet is None and triplet_sum is None:
                triplet = [val, l_val, r_val]
                triplet_sum = check_sum

            check_diff = abs(check_sum - target)
            triplet_diff = abs(triplet_sum - target)

            if check_diff < triplet_diff or (check_diff == triplet_diff and check_sum < triplet_sum):
                triplet = [val, l_val, r_val]
                triplet_sum = check_sum
            
            if check_sum > target:
              r -= 1
            else:
              l += 1

    return triplet_sum

def triplets_with_smaller_sum(nums: List[int], target: int) -> int:
    """ Given an unordered list of ints, return all triplets that sum to less than target.
        Time complexity: O(n^2)
        Space complexity: O(n)
    """

    sorted_nums = sorted(nums)
    count = 0

    def count_pairs(curr_val: int, curr_idx: int):
        l, r = len(sorted_nums) - 2, len(sorted_nums) - 1
        count = 0

        while r > curr_idx + 1:
            while l > curr_idx:
                l_val, r_val = sorted_nums[l], sorted_nums[r]

                if l_val + r_val + curr_val < target:
                    count += l - curr_idx
                    break

                l -= 1

            r -= 1
            l = r - 1
        
        return count

    for i, val in enumerate(sorted_nums):
        if val >= target / 3 or i >= len(sorted_nums) - 2:
            break
        count += count_pairs(val, i)

    return count

def subarrays_product_less_than_target(nums: List[int], target: int) -> List[List[int]]:
    """ Returns all contiguous subarrays whose elements, when multiplied, are less than target.
            Assumes all positive integers, positive target
        Time complexity: O(n^2)
        Space complexity: O(n * (n * (n + 1) / 2)) => O(n^3)
    """
    from functools import reduce

    subarrays = []
    l, r = 0, 1

    while l < len(nums):
        if (l_val := nums[l]) < target:

            subarrays.append([l_val])

            while r < len(nums):
                if reduce(lambda x, y: x * y, nums[l:r + 1]) < target:
                    r += 1
                    subarrays.append(nums[l:r])
                else:
                    break

                l
        l += 1
        r = l + 1

    return subarrays


def dutch_flag_problem(nums: List[int]) -> None:
    """ Sorts an array of numbers (to be treated like objects) in place.
        Time complexity: O(n)
        Space complexity: O(1)
    
        Post-submission notes: Do this one again
    """

    l, r = 0, len(nums) - 1

    last_zero, first_two = 0, len(nums) - 1  

    i = 0
    while i <= first_two:
        
        if nums[i] == 0:
            nums[i], nums[last_zero] = nums[last_zero], nums[i]
            i += 1
            last_zero += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[first_two] = nums[first_two], nums[i]
            first_two -= 1


""" Challenge problems """

def quad_sum_to_target(nums: List[int], target: int) -> List[List[int]]:
    """ Returns all sets of 4 elements that sum to target
        Time complexity: O(n^3)
        Space complexity: O(n) - sorting, again
    """
    nums.sort()

    quads = []

    for i in range(len(nums) - 3):
        val_i = nums[i]

        # Skip duplicates
        if i > 0 and val_i == nums[i - 1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            val_j = nums[j]

            # Skip duplicates
            if j > i + 1 and val_j == nums[j - 1]:
                continue
        
            l, r = j + 1, len(nums) - 1

            while r > l:
                l_val, r_val = nums[l], nums[r]
                s = val_i + val_j + l_val + r_val

                if s == target:
                    quads.append([val_i, val_j, l_val, r_val])
                    l += 1
                    r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1

    return quads

def backspace_compare(s1: str, s2: str) -> None:
    """ Compares two strings where # represents a backspace.
        Time complexity: O(len(s1) + len(s2))
        Space complexity: O(len(s1) + len(s2))

        Post-submission notes: Review given solution for space complexity reduction
    """

    def resolve_backspaces(s: str) -> str:
        l, r = 0, 1
        BS = "#"
        s_list = list(s)

        while s_list[l] == BS:
            l += 1
            r += 1

        while r < len(s_list):

            if s_list[r] != BS:
                l += 1
                r += 1
                continue
            while r < len(s_list) and s_list[r] == BS:
                s_list.pop(r)
                s_list.pop(l)

                # Handle consecutive backspaces
                if l < len(s_list) and s_list[l] == BS:
                    l -= 1
                    r -= 1

        return "".join(s_list)
    
    return resolve_backspaces(s1) == resolve_backspaces(s2)

def minimum_window_sort(nums: List[int]):
    """ Returns the length of the shortest subarray that needs to be sorted in order for the full list to be sorted.
        Time complexity: O(n)
        Space complexity: O(1)
        
        Post-submission notes: Review, missed edge case
    """

    l, r = 0, len(nums) - 1

    while r > 0 and nums[r] >= nums[r - 1]:
        r -= 1
    while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
        l += 1

    # Already sorted
    if l == len(nums) - 1:
        return 0

    sub_max = None
    sub_min = None

    # Get minimum and maximums of current subarray
    for i in range(l, r + 1):
        if sub_max is None:
            sub_max = nums[i]
            sub_min = nums[i]
            continue
        sub_max = max(sub_max, nums[i])
        sub_min = min(sub_min, nums[i])

    # Extend toward beginning w.r.t. sub_min
    while l > 0 and nums[l - 1] > sub_min:
        l -= 1
    # Extend toward end w.r.t. sub_max
    while r < len(nums) - 1 and nums[r + 1] < sub_max:
        r += 1

    return r + 1 - l
