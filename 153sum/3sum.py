class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums= sorted(nums, reverse=True)
        n = len(nums)
        print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            #print(i,left, right, n)

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                #print(nums[i], nums[left], nums[right], total)
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total< 0:
                    right -= 1
                else:
        
                    left +=1
        #print(ans)
        return ans