class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            val = target - numbers[left]
            if numbers[right] == val:
                return [left+1, right+1]
            elif numbers[right]> val:
                right -=1
            else:
                left +=1 