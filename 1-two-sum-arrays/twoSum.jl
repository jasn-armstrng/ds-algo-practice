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

#  Brute force: O(n^2) solution. nums[1..n] * nums[1..n]
function twoSum(nums=[], target=int)
  for i in eachindex(nums), j in eachindex(nums)
    if (i != j) && (nums[i]+nums[j] == target)
      return nums[i], nums[j]
    end
  end
  return [-1, -1]
end

@time twoSum([8, 7, 2, 5, 3, 1], 10)
println(twoSum([8, 7, 2, 5, 3, 1], 10))
# Tests:
# println(twoSum([5, 2, 6, 8, 1, 9], 12))
# println(twoSum([1, 1, 1, 1], 2))
# println(twoSum([80, 40, 30, 60], 140))
