class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #two pointers,p1 =pointer for t and p2 pointer for s
        p1=p2=0
        while p1 < len(t) and p2 < len(s):
            if(t[p1] == s[p2]):
                p2+=1
            p1+=1
        return p2 == len(s)

    


