/*
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example,
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
*/
#include <iostream>
#include <vector>

class Solution {
  public:
    std::vector<int> running_sum(const std::vector<int> nums) {
      // calculate the running sum of the elements in array
      // pre-conditions: Array size 1-1000, elements between -10^6 and 10^6
      // post-conditions: return running some in vector. Don't modify original
      std::vector<int> output;
      int sum = 0;
      for (int n: nums) {
        sum += n;
        output.push_back(sum);
      }
      return output;
    }
};

int main() {

  return 0;
}
