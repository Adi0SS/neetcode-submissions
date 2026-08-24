import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    pop_order_list = []
    loop_run_times = len(heap)
    for i in range(loop_run_times):
        pop_order_list.append(heapq.heappop(heap))
    return pop_order_list    

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
