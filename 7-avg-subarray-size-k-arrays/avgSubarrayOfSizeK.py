# Question: Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

# Note we are never checking a window of size K starting from each index, we are calculating what's inside the
# sliding window.

def findAveragesOfOfSubarrays(K, arr=[]):
    result=[]
    windowSum=0.0
    windowStart=0

    for windowEnd in range(len(arr)):
        # print("windowEnd: {}".format(windowEnd))
        windowSum+=arr[windowEnd]
        # print("windowSum: {}".format(windowSum))

        if windowEnd>=K-1:
            # print(windowSum/K)
            result.append(windowSum/K)
            windowSum-=arr[windowStart]
            windowStart+=1

    return result

# def main():
#     result = findAveragesOfOfSubarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
#     print("Averages of subarrays of size K: " + str(result))

# main()
