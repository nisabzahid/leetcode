class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0]* l 
        st = []
        for i in range(l):
            if not st:
                st.append(i)
            else:
                # print(temperatures[st[-1]], temperatures[i], i)
                while st and temperatures[st[-1]] < temperatures[i]:
                        # print(temperatures[st[-1]], temperatures[i], i)
                        t = st.pop()
                        ans[t] = i-t
                        # print(ans[t], t, i)
                st.append(i)
        while st:
            ans[st.pop()] = 0
        return ans