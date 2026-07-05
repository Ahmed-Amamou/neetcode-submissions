class Solution:
    def validPalindrome(self, s: str) -> bool:
        #idea: have two pointers; i: one starts at index 0 and, j:  other at the end 
        # i increments while j decrements, (only if caracters match)
        #if they don't we compare (i+1)th caracter with with (j)th if no match 
        #we compare the i-th caracter with the (j-1)th if no match we retrun False
        #if we do have a match : in the (i+1)th & jth case : we discard i-th caracter 
        #in the other case the jth caracter

        mismatch = False
        essay1 = True
        essay2 = True
        l=0
        r = len(s)-1
        while(l < r and r>=0 and l <len(s)):
            print("l: ",l, "r :",r )
            print("-> ",s[l],"   ", s[r] )
            if s[l] != s[r] :
                print("mismatch")
                if not mismatch and (s[l+1] == s[r] or s[l] == s[r-1]):
                    if s[l] == s[r-1] :
                        mismatch = not mismatch
                        r-=1
                        print("deleted right: ", s[r])
                    elif s[l+1] == s[r]:
                        mismatch = not  mismatch
                        l+=1
                        print("deleted left: ", s[l])
                else:
                    print(s," is Not valid palindrome!")
                    essay1 =  False
                    break
                
            l+=1
            r-=1
        print("----------------------------")
        l=0
        r = len(s)-1
        mismatch = False
        while(l < r and r>=0 and l <len(s)):
            print("l: ",l, "r :",r )
            print("-> ",s[l],"   ", s[r] )
            if s[l] != s[r] :
                print("mismatch")
                if not mismatch and (s[l+1] == s[r] or s[l] == s[r-1]):
                    if s[l+1] == s[r]:
                        mismatch = not  mismatch
                        l+=1
                        print("deleted left: ", s[l])
                    elif s[l] == s[r-1] :
                        mismatch = not mismatch
                        r-=1
                        print("deleted right: ", s[r])
                else:
                    print(s," is Not valid palindrome!")
                    essay2 =  False
                    break
                
            l+=1
            r-=1
        return essay1 or essay2

                

