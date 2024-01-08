#bruteforce solution. have to make it faster
#  with sliding window approach
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 ,ls2 = len(s1)-1, len(s2)-1
        if ls1>ls2:
            return False
        sorted_s1 = sorted(s1) #O(NlogN)
        for i in range(ls2-ls1+1):#O(N)
            if sorted_s1 == sorted(s2[i:i+ls1+1:]): #O(N+NlogN)
                return True
        return False

## sliding window solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 ,ls2 = len(s1), len(s2)
        if ls1>ls2:
            return False
        s1_list = [0]*26
        s2_list = [0]*26
        for i in range(0, ls1):
            s1_list[ord(s1[i])-ord('a')] +=1
            s2_list[ord(s2[i])-ord('a')] +=1
        if s1_list == s2_list:
            return True
        
        #sliding window 
        for i in range(ls1,ls2):
            s2_list[ord(s2[i]) - ord('a')] += 1
            s2_list[ord(s2[i-ls1])- ord('a')] -= 1
            if s1_list == s2_list:
                return True
        
        return False

##Let's analyze the time complexity of both the brute-force and sliding window approaches.
# Brute-force Approach:
# Sorting s1:
# O(N log N ), where


# N is the length of s1.
# Iterating through s2 using a sliding window:

# O(N×(N+N log N)), where

# N is the length of s2.
# The overall time complexity of the brute-force approach is approximately
# O(N^2+NlogN).
# Sliding Window Approach:
# Initializing two arrays s1_list and s2_list:

# O(26)=O(1) since the size of the arrays is constant.
# Filling the initial counts for the first window of s2 and s1:
# O(N)
# O(N), where


# N is the length of s1.
# Sliding window through s2:
# O(N).
# The overall time complexity of the sliding window approach is
# O(N).
