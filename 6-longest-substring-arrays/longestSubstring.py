# Question: Leetcode 3

def lenLongestSubstring(s=str):
    stringLength=len(s)
    elementOccurence={}
    window=[]
    output=0

    for i in range(0, stringLength):
        e = s[i]
        if e not in elementOccurence:
            elementOccurence[e]=1
            window.append(e)
            print(window)
            if len(window)>output:
                output=len(window)
        else:
            elementOccurence={e:1}
            window=[e]
            print(window)

    return output

# Not yet correct.
