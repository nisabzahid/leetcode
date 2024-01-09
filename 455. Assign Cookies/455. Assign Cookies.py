# sort and use two pointer solution
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        fi=se=0
        while fi <= len(g)-1 and se <= len(s)-1 :
            if g[fi] <= s[se]:
                fi +=1
                se +=1
            elif g[fi] > s[se]:
                fi +=1
            else:
                se +=1
        return se