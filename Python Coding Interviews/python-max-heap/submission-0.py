import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    temp_list = []
    return_list = []
    for num in nums:
        heapq.heappush(temp_list, -num)
    for i in range(len(nums)):
        return_list.append(-heapq.heappop(temp_list))

    return return_list    





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
