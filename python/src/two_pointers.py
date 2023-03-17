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
