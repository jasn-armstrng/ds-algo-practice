# Question:
# Given an unsorted integer array, find a pair with the given sum in it.
# - Each input can have multiple solutions. The output should match with
#   either one of them.

# Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
# Output: (8, 2) or (7, 3)

# - The solution can return pair in any order. If no pair with the given
#   sum exists, the solution should return the pair (-1, -1).

# Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
# Output: (-1, -1)

import cProfile as profile
import pstats

#  Brute force: O(n^2) solution. nums[1..n] * nums[1..n]
# def twoSum(nums=[], target=int):
#     for i,j in enumerate(nums):
#         for k,l in enumerate(nums):
#             if i!=k and j+l==target:
#                 return (j,l)
#     return (-1, -1)

# O(n) solution. 2 distinct traversals of nums[1..n]
def twoSum(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        hashMap[nums[i]]=i

    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in hashMap and hashMap[complement] != i:
            return (i, hashMap[complement])
      
    return (-1, -1)


if __name__=='__main__':
    # call function twoSum with profiling
    prof = profile.Profile()
    prof.enable()
    twoSum([8, 7, 2, 5, 3, 1], 10)
    prof.disable()

    # print profiling output
    stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
    stats.print_stats(10) # top 10 rows
