# Question: Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.

# O(n) solution
# Solution is from designgurus course on sliding window. For reference
def longestSubstring(s=str, k=int):
    windowStart=0
    maxLength=0
    charFrequency={}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for windowEnd in range(len(s)):
        rightChar=s[windowEnd]
        if rightChar not in charFrequency:
            charFrequency[rightChar]=0 # create hash entry before incrementing frequnecy
        charFrequency[rightChar]+=1

        # shrink the sliding window, until we are left with 'k' distinct characters in
        # the char_frequency
        while len(charFrequency)>k:
            leftChar=s[windowStart]
            charFrequency[leftChar]-=1
            if charFrequency[leftChar]==0:
                del charFrequency[leftChar]
            windowStart+=1  # shrink the window
        maxLength=max(maxLength, windowEnd-windowStart+1)
    return maxLength
