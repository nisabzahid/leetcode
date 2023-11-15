


#basic binary search


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        middle = ceil((1 + n) // 2 ) 
        while guess(middle) != 0 :
            num = guess(middle)
            if num == -1:
                end = middle-1
            if num == 1:
                start = middle+1
            middle  = int(ceil((start + end)//2))
        return int(middle)