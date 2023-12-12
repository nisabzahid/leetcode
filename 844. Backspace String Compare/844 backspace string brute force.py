class Solution(object):
    def createList(self, s):
        array = []
        for i in s:
            if i =='#':
                if len(array) != 0:
                    array.pop()
            else:
                array.append(i)
        return array

    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.createList(s) == self.createList(t)

        