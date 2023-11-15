

# loop through the array until tickets[k] = 0 
# if tickets[i] != 0  then increase time and decrease the tickets[i]
# reset the iterator i value when it gets to the len of the tickets array by i  = (i+1) % len(tickets)

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        i = 0
        while tickets[k]> 0 :
            if tickets[i] != 0 :
                tickets[i] -= 1
                time += 1

            i  = (i+1) % len(tickets)
        return time