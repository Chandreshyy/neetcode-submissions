class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in tokens:
            print(i, stack)
            if not i.lstrip('-').isdigit():
                print(i)
                prev1 = int(stack.pop())
                prev2 = int(stack.pop())
                print(prev1, prev2)
                if i == '+':
                    stack.append(prev1+prev2)
                elif i == '-':
                    stack.append(prev2-prev1)
                elif i == "*":
                    stack.append(prev1*prev2)
                else:
                    stack.append(int(prev2/prev1))
            else:
                stack.append(i)
        
        return int(stack[0])
        