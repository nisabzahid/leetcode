class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)
        return dic.values()

        #this appoach gives time limit
        # if len(strs) == 0:
        #     return [[""]]
        # ans = []
        # ans.append([strs[0]])
        
        # for key,value in enumerate(strs):
        #     if key == 0:
        #         continue
        #     insert = 0
        #     for item in ans:
        #         if sorted(item[0]) == sorted(value):
        #             item.append(value)
        #             insert = 1
        #             break
        #     if insert == 0:
        #         ans.append([value])
        # return ans