from heapq import heapify, heappush, heappop
import heapq
from typing import List

class MedianOfAStream:

    second_half = [] # min heap
    first_half = [] # max heap

    def insert_num(self, num):
        # Initial insert
        if not self.first_half or -self.first_half[0] >= num:
            heappush(self.first_half, -num)
        else:
            heappush(self.second_half, num)

        # Rebalance when necessary
        if len(self.first_half) > len(self.second_half) + 1:
            heappush(self.second_half, -heappop(self.first_half))
        elif len(self.second_half) > len(self.first_half):
            heappush(self.first_half, -heappop(self.second_half))

    def find_median(self):
        if len(self.second_half) != len(self.first_half):
            return -1 * self.first_half[0]
        else:
            return (self.second_half[0] + -1 * self.first_half[0]) / 2

class SlidingWindowMedian:
    """ Partial Solution """

    max_heap = []
    min_heap = []

    def find_sliding_window_median(self, nums: List[int], k: int) -> List[float]:
        medians = [0.0 for _ in range(len(nums) - k + 1)]

        for i in range(len(nums)):
            num = nums[i]

            if not self.max_heap or num <= -self.max_heap[0]:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)
            print("Before")
            print(self.min_heap)
            print(self.max_heap)
            self.rebalance_heaps()
            print("After")
            print(self.min_heap)
            print(self.max_heap)
            result_idx = i - k + 1

            if result_idx >= 0:
                print(result)
                if len(self.max_heap) == len(self.min_heap):
                    medians[result_idx] = (-self.max_heap[0] + self.min_heap[0]) / 2
                else:
                    medians[result_idx] = -self.max_heap[0]

                # Remove the element leaving the window
                to_delete = nums[result_idx]

                if -to_delete <= self.max_heap[0]:
                    self.remove_from_heap(self.max_heap, -to_delete)
                else:
                    self.remove_from_heap(self.min_heap, to_delete)
   

    def rebalance_heaps(self) -> None:
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


    def remove_from_heap(self, heap: List[int], num: int) -> None:
        idx = heap.index(num)

        heap[idx] = heap[-1]
        del heap[-1]

        # TODO: Learn about sifting to make this faster
        heapify(heap)
