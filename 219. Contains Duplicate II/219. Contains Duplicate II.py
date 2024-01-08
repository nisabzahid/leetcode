class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        d = defaultdict(lambda: float('-inf'))
        for i in range(0,len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k :
                    return True
            else:
               d[nums[i]]= max(d[nums[i]] , i) #update the index with bigger index
        return False