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
    


# faster solution with set
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:return False
        set_=set()
        for r in range(len(nums)):
            if nums[r] in set_:return True
            set_.add(nums[r])
            if len(set_)==k+1:set_.remove(nums[r-k])
            #lenth of set is k, if it becomes larger than k ,
            #then remove the last element from the set
        return False