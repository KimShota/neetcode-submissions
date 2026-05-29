class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        stack = []

        for p in s:
            if p in pair:
                stack.append(p)

            if p not in pair:
                if not stack:
                    return False
                cur = stack.pop()
                if cur is None:
                    return False
                if p != pair[cur]:
                    return False 
        if stack:
            return False 
            
        return True
                
        