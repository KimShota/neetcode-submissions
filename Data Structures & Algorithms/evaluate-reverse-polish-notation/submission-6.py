class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        if len(tokens) == 1:
            return int(tokens[0])

        for t in tokens: 
            if t == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                result = b + a
                stack.append(result)
            elif t == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                result = b - a 
                stack.append(result)
            elif t == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                result = b * a
                stack.append(result)
            elif t == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                result = int(b / a)
                stack.append(result)
            else:
                stack.append(int(t))
        return result
                