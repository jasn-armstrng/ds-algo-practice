# Question:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of
# all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums=[]):
    productArray=[]
    n = len(nums)

    # O(n^2) solution
    for i in range(0,n):
        product=1
        for j in range(0,n):
            if i!=j:
                product*=nums[j]
        productArray.append(product)
    return productArray


# Test
# print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))
# print(productExceptSelf([0,0]))
# print(productExceptSelf([1,1]))
# print(productExceptSelf([1,0,0,0]))
