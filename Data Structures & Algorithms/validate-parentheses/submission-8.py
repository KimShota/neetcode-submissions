class Solution:
    def isValid(self, s: str) -> bool:
        parent = {
            ']': '[', 
            ')': '(', 
            '}': '{'
        }

        stack = []

        for p in s:
            if p in parent and stack:
                a = stack.pop()
                if a != parent[p]:
                    return False
                else:
                    continue 
            
            stack.append(p)

        if not stack:
            return True
        else:
            return False

            