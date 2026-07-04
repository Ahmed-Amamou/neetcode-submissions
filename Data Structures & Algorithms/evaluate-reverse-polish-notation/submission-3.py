class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #division if float -> rounded up if negative, rounded down if positive
        def is_number(s: str) -> bool:
            try:
                float(s)
                return True
            except ValueError:
                return False
        stack = []
        res = 0
        operations = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x-y,
            '/': lambda x,y: int(x/y),
            '*': lambda x,y: x*y
            }
        for x in tokens:
            print(x)
            if is_number(x):
                stack.append(int(x))
                print("number added: ", int(x))
            else:
                print("operation: ", (x))
                first = stack.pop()
                second = stack.pop()
                stack.append(operations[x](second,first))
            print("stack state : ",stack)

        return stack.pop()
                

        