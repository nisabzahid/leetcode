from typing import List
class Solution:

    def check(self, a, b, nums):
        l = []
        for i  in range(a, a+3):
            for j in range(b, b+3):
                if i < len(nums) and j < len(nums[i]) and  nums[i][j] != '.' and nums[i][j] in '123456789' :
                    l.append(int(nums[i][j]))
        # print(len(l) == len(list(set(l))) ,"1")
        # if len(l) != len(list(set(l))):
        #     print(l,"board", a, b)
        return len(l) == len(list(set(l))) 

    def checkrow(self, a, b, nums):
        l = []
        i = a
        for j in range(9):
            if j < len(nums[i]) and nums[i][j] != '.' and nums[i][j] in '123456789':
                l.append(int(nums[i][j]))
        # print(len(l) == len(list(set(l))) ,"2")
        return len(l) == len(list(set(l)))
    
    def checkcolumn(self, a, b, nums):
        l = []
        j = b
        for i in range(9):
            if  i < len(nums[j]) and nums[i][j] != '.' and nums[i][j] in '123456789' :
                l.append(int(nums[i][j]))
        # print(len(l) == len(list(set(l))) ,"3")
        return len(l) == len(list(set(l)))
    


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0 :
                    if self.check(i, j, board) == False:
                        return False
                if i == 0:
                    if self.checkcolumn(i, j, board) == False:
                        return False
                
                if j == 0:
                    if self.checkrow( i, j, board) == False:
                        return False
            
        return True 