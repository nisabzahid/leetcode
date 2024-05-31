class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n, nums = len(matrix)
        nums = set(range(1, n + 1))
        for i in range(n):
            rows = set(matrix[i])
            cols = set(matrix[j][i] for j in range(n))
            if rows != nums or cols != nums:
                return False

        return True
