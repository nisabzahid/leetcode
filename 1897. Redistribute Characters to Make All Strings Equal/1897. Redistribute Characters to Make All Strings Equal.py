class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = defaultdict(int)
        for word in words:
            for ch in word:
                d[ch] = d[ch]+1
        #print(d, len(words))
        for i in d:
            if  d[i] % len(words) !=0:
                #print(d[i])
                return False
        return True 