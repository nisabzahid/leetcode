class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small = word1 if len(word1) <= len(word2) else word2
        big = word1 if len(word1) >= len(word2) else word2
        ans= ""
        for s in range(len(small)):
            ans = ans+ word1[s]+word2[s]
        for c in range(len(small),len(big)):
            ans = ans+ big[c]
        return ans