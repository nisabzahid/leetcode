from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            key = str(num)
            if d[key] != None :
                d[key] = d[key] +1
            else:
                d[key]= 1
        
        s = sorted(d.items(), key=lambda x:x[1], reverse=True )
        ans= [ ]
        # print(d)
        for key,_ in s:
            ans.append(int(key))
            if len(ans) == k:
                return ans