# Question: Contains Duplicate
# Source: https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums=[]) -> bool:
    hashMap={}
    n=len(nums)
    for i in range(0,n): # O(n)
        if nums[i] in hashMap:
            return True
        else:
            hashMap[nums[i]]=1
    return False
