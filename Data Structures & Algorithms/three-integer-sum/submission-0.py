class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #store unique elements in a dictionary with values being a list of indices (occurences)
        n = len(nums)
        D = {}
        for i, ele in enumerate(nums):
            if ele in D:
                D[ele].append(i)
            else:
                D[ele] = [i]
        
        pre_ans = []
        for i in range(n-2):
            for j in range(i+1,n-1):
                if -(nums[i] + nums[j]) in D:
                    for k in D[-(nums[i] + nums[j])]:
                        if k!=i and k != j:
                            local = [nums[i],nums[j], -(nums[i] + nums[j])]
                            pre_ans.append(tuple(sorted(local)))
                            if local == [0,0,0]:
                                break
        ans = set(pre_ans)
        return list(ans)

