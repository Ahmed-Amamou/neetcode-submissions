class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        row = 0
        while(n>0):
            n-=i
            if n<0:
                return row
            row+=1;
            i+=1;

        return row