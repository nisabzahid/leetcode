class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        charvals = brackets.values()
        charkeys =  brackets.keys()
        for char in s:
            if char in charvals:
                stack.append(char)
            elif char in charkeys:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                return False
        
        return not stack
