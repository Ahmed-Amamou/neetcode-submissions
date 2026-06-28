class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        D = {'(':')','[':']','{':'}'}
        for c in s:
            if c in ['{','(','[']:
                stack.append(c)
            else:
                if stack!=[]:
                    opener = stack.pop()
                    if D[opener] == c:
                        continue
                    else:
                        return False
                else :  
                    return False
            print(stack)
        if stack==[]:
            return True
        else: 
            return False