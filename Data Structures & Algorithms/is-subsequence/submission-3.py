class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #two pointers,p1 =pointer for t and p2 pointer for s
        p1=p2=0
        if s =="":
            return True
        if len(s)>len(t):
            return False
        while(True):
            while(True):
                if s[p2] == t[p1]:
                    p2+=1
                p1+=1
                break
            if p2>=len(s):
                return True
            if p1>=len(t):
                    break

        if p2>=len(s):
            return True
        else:
            return False
    


