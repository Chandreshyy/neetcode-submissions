class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if not i.lstrip('-').isdigit():
                prev1 = int(stack.pop())
                prev2 = int(stack.pop())
                if i == '+':
                    stack.append(prev1+prev2)
                elif i == '-':
                    stack.append(prev2 - prev1)
                elif i == "*":
                    stack.append(prev1*prev2)
                else:
                    stack.append(int((prev2/prev1)))
            else:
                stack.append(i)
            print(stack)
        
        return int(stack[0])

        