# my initial solution that was n3 and improved it to n2.
# but still it is getting tle
# appropriate solution is o(n) of two pointers
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         a = []
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i]<nums[j]:
#                     a.append([i,j])
#         for i in range(len(nums)):
#             for ar in a:
#                 if i <ar[0]< ar[1] and nums[i] < nums[ar[0]] < nums[ar[1]]:
#                     return True
        
#         return False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False