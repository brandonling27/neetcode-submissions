class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = { '}': '{', ')': '(', ']': '['}
        for b in s:
            if b not in closing: 
                stack.append(b)
            elif (stack and stack[-1] != closing[b]) or not stack:
                return False
            elif stack:
                stack.pop()
        print(stack)
        return not stack
    