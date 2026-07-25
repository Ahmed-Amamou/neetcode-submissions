class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        X = set(nums)
        nums = sorted(list(X))
        mx = 0
        n = len(nums)
        if n <= 1 :
            return n
        
        i=1
        local = 1
        print(nums)
        while(i<n):
            if nums[i]==(nums[i-1]+1):
                local +=1
            else:
                local = 1
            print(f"i:{i}, local: {local}")
            mx = max(local,mx)
            i+=1

        return mx

        
