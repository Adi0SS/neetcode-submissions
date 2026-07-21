from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    summation = 0
    for num in nums:
        summation +=  num
    return summation    

def get_min(nums: List[int]) -> int:
    Minimum = nums[0]
    for num in nums:
        if num <= Minimum: Minimum = num
    return Minimum

def get_max(nums: List[int]) -> int:
    Maximum = nums[0]
    for num in nums:
        if num >= Maximum: Maximum = num
    return Maximum    




# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
