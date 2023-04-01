from heapq import heappush, heappop


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
